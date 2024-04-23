---
title: "开源大型语言模型作为LangChain智能体" 
thumbnail: /blog/assets/open-source-llms-as-agents/thumbnail_open_source_agents.png
authors:
- user: m-ric
- user: Jofthomas
- user: andrewrreed
---
# 开源大型语言模型作为LangChain智能体

## 简而言之

开源大型语言模型（LLMs）现已达到了一定的性能水平，使其可以成为推动代理工作流程的合理推理引擎：[Mixtral](https://huggingface.co/blog/mixtral) 在我们的基准测试中甚至[超越了 GPT-3.5](#results)，并且通过微调，其性能可以轻松进一步增强。

## 引言

经过[因果语言建模](https://huggingface.co/docs/transformers/tasks/language_modeling)训练的大型语言模型（LLMs）能够处理广泛的任务，但它们通常在逻辑、计算和搜索等基本任务上存在困难。最糟糕的情况是，它们在某个领域（如数学）表现不佳，却仍然尝试自行处理所有计算。

为了克服这一弱点，其中一个方法是将LLM集成到一个能够调用工具的系统中：这样的系统被称为LLM智能体。

在这篇文章中，我们将解释ReAct智能体的内部工作原理，然后展示如何使用最近集成到LangChain中的`ChatHuggingFace`类来构建它们。最后，我们将对几个开源的LLM与GPT-3.5和GPT-4进行基准测试。

## Table of Contents

- [什么是智能体？](#what-are-agents)
  - [ReAct智能体内部运作的简单例子](#toy-example-of-a-react-agents-inner-working)
  - [智能体系统的挑战](#challenges-of-agent-systems)
- [使用LangChain运行智能体](#running-agents-with-langchain)
- [智能体对决：不同LLM作为通用推理智能体的表现如何？](#agents-showdown-how-do-open-source-llms-perform-as-general-purpose-reasoning-agents)
  - [评估](#evaluation)
  - [结果](#results)

## 什么是智能体？

LLM智能体的定义相当广泛：LLM智能体是所有使用LLM作为其引擎并能够基于观察对环境执行操作的系统。它们可以使用多次感知 ⇒ 反思 ⇒ 行动的循环来完成任务，并且通常通过规划或知识管理系统来增强其性能。你可以在[Xi等人，2023年](https://huggingface.co/papers/2309.07864)的文章中找到关于智能体领域的良好回顾。

今天，我们关注的是**ReAct智能体**。[ReAct](https://huggingface.co/papers/2210.03629) 是一种基于两个词汇“**推理**”和“**行动**”组合而成的建立智能体的方法。在提示中，我们描述了模型、它可以使用的工具，并要求它“一步一步地”思考（也被称为[思维链](https://huggingface.co/papers/2201.11903)行为），以规划和执行其下一步动作，以达到最终答案。

<p align="center">
    <img src="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/open-source-llms-as-agents/ReAct.png" alt="drawing" width=90%>
</p>


### Toy example of a ReAct agent's inner working

The graph above seems very high-level, but under the hood it’s quite simple.

Take a look at [this notebook](https://colab.research.google.com/drive/1j_vsc28FwZEDocDxVxWJ6Fvxd18FK8Gl?usp=sharing): we implement a barebones tool call example with the Transformers library. 

The LLM is called in a loop with a prompt containing in essence:

```
Here is a question: "{question}" 
You have access to these tools: {tools_descriptions}. 
You should first reflect with ‘Thought: {your_thoughts}’, then you either:
- call a tool with the proper JSON formatting,
- or your print your final answer starting with the prefix ‘Final Answer:’
```

Then you parse the LLM’s output:

- if it contains the string `‘Final Answer:’`, the loop ends and you print the answer,
- else, the LLM should have output a tool call: you can parse this output to get the tool name and arguments, then call said tool with said arguments. Then the output of this tool call is appended to the prompt, and you call the LLM again with this extended information, until it has enough information to finally provide a final answer to the question.

For instance, the LLM's output can look like this, when answering the question: `How many seconds are in 1:23:45?`
```
Thought: I need to convert the time string into seconds.

Action:
{
    "action": "convert_time",
    "action_input": {
    "time": "1:23:45"
    }
}
```

Since this output does not contain the string `‘Final Answer:’`, it is calling a tool: so we parse this output and get the tool call parameters: call tool `convert_time` with arguments `{"time": "1:23:45"}`.
Running this tool call returns `{'seconds': '5025'}`.

So we append this whole blob to the prompt.

The new prompt is now (a slightly more elaborate version of):
```
Here is a question: "How many seconds are in 1:23:45?"
You have access to these tools:
    - convert_time: converts a time given in hours:minutes:seconds into seconds.

You should first reflect with ‘Thought: {your_thoughts}’, then you either:
- call a tool with the proper JSON formatting,
- or your print your final answer starting with the prefix ‘Final Answer:’

Thought: I need to convert the time string into seconds.

Action:
{
    "action": "convert_time",
    "action_input": {
    "time": "1:23:45"
    }
}
Observation: {'seconds': '5025'}
```

➡️ We call the LLM again, with this new prompt. Given that it has access to the tool call's result in `Observation`, the LLM is now most likely to output:

```
Thought: I now have the information needed to answer the question.
Final Answer: There are 5025 seconds in 1:23:45.
``````

And the task is solved!

### Challenges of agent systems

Generally, the difficult parts of running an agent system for the LLM engine are:

1. From supplied tools, choose the one that will help advance to a desired goal: e.g. when asked `"What is the smallest prime number greater than 30,000?"`, the agent could call the `Search` tool with `"What is he height of K2"` but it won't help.
2. Call tools with a rigorous argument formatting: for instance when trying to calculate the speed of a car that went 3 km in 10 minutes, you have to call tool `Calculator` to divide `distance` by `time` : even if your Calculator tool accepts calls in the JSON format: `{”tool”: “Calculator”, “args”: “3km/10min”}` , there are many pitfalls, for instance:
    - Misspelling the tool name: `“calculator”` or `“Compute”` wouldn’t work
    - Giving the name of the arguments instead of their values: `“args”: “distance/time”`
    - Non-standardized formatting: `“args": "3km in 10minutes”`
3. Efficiently ingesting and using the information gathered in the past observations, be it the initial context or the observations returned after using tool uses.


So, how would a complete Agent setup look like?

## Running agents with LangChain

We have just integrated a `ChatHuggingFace` wrapper that lets you create agents based on open-source models in [🦜🔗LangChain](https://www.langchain.com/).

The code to create the ChatModel and give it tools is really simple, you can check it all in the [Langchain doc](https://python.langchain.com/docs/integrations/chat/huggingface). 

```python
from langchain_community.llms import HuggingFaceHub
from langchain_community.chat_models.huggingface import ChatHuggingFace

llm = HuggingFaceHub(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
)

chat_model = ChatHuggingFace(llm=llm)
```

You can make the `chat_model` into an agent by giving it a ReAct style prompt and tools:

```python
from langchain import hub
from langchain.agents import AgentExecutor, load_tools
from langchain.agents.format_scratchpad import format_log_to_str
from langchain.agents.output_parsers import (
    ReActJsonSingleInputOutputParser,
)
from langchain.tools.render import render_text_description
from langchain_community.utilities import SerpAPIWrapper

# setup tools
tools = load_tools(["serpapi", "llm-math"], llm=llm)

# setup ReAct style prompt
prompt = hub.pull("hwchase17/react-json")
prompt = prompt.partial(
    tools=render_text_description(tools),
    tool_names=", ".join([t.name for t in tools]),
)

# define the agent
chat_model_with_stop = chat_model.bind(stop=["\nObservation"])
agent = (
    {
        "input": lambda x: x["input"],
        "agent_scratchpad": lambda x: format_log_to_str(x["intermediate_steps"]),
    }
    | prompt
    | chat_model_with_stop
    | ReActJsonSingleInputOutputParser()
)

# instantiate AgentExecutor
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

agent_executor.invoke(
    {
        "input": "Who is the current holder of the speed skating world record on 500 meters? What is her current age raised to the 0.43 power?"
    }
)
```

And the agent will process the input:

```markdown
Thought: To answer this question, I need to find age of the current speedskating world record holder.  I will use the search tool to find this information.
Action:
{
    "action": "search",
    "action_input": "speed skating world record holder 500m age"
}
Observation: ...
```

## Agents Showdown: how do open-source LLMs perform as general purpose reasoning agents?

You can find the code for this benchmark [here](https://github.com/aymeric-roucher/benchmark_agents/).

### Evaluation

We want to measure how open-source LLMs perform as general purpose reasoning agents. Thus we select questions requiring using logic and the use of basic tools: a calculator and access to internet search.
The [final dataset](https://huggingface.co/datasets/m-ric/agents_small_benchmark) is a combination of samples from 3 other datasets:

- For testing Internet search capability: we have selected questions from [HotpotQA](https://huggingface.co/datasets/hotpot_qa): this is originally a retrieval dataset, but it can be used for general question answering, with access to the internet. Some questions originally need to combine information from various sources: in our setting, this means performing several steps of internet search to combine the results.
- For calculator usage, we added questions from [GSM8K](https://huggingface.co/datasets/gsm8k): this dataset tests grade-school math ability, and is entirely solvable by correctly leveraging the 4 operators (add, subtract, multiply, divide).
- We also picked questions from [GAIA](https://huggingface.co/papers/2311.12983), a very difficult benchmark for General AI Assistants. The questions in the original dataset can require many other different tools, such as a code interpreter or pdf reader: we hand-picked questions that do not require other tools than search and calculator.

Evaluation was performed with GPT-4-as-a-judge using a prompt based on the [Prometheus prompt format](https://huggingface.co/kaist-ai/prometheus-13b-v1.0), giving results on a 5-point Likert Scale: see the exact prompt [here](https://github.com/aymeric-roucher/benchmark_agents/blob/master/scripts/prompts.py).

### Models

We evaluate a few strong open-source models:
- [Llama2-70b-chat](https://huggingface.co/meta-llama/Llama-2-70b-chat-hf)
- [Mixtral-8x7B-Instruct-v0.1](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1)
- [OpenHermes-2.5-Mistral-7B](https://huggingface.co/teknium/OpenHermes-2.5-Mistral-7B)
- [Zephyr-7b-beta](https://huggingface.co/HuggingFaceH4/zephyr-7b-beta)
- [SOLAR-10.7B-Instruct-v1.0](https://huggingface.co/upstage/SOLAR-10.7B-Instruct-v1.0)

These models are evaluated in LangChain's [ReAct implementation](https://github.com/langchain-ai/langchain/tree/021b0484a8d9e8cf0c84bc164fb904202b9e4736/libs/langchain/langchain/agents/react)
This means we prompt them to output their function calls in this format:

```json
{
  "action": $TOOL_NAME,
  "action_input": $INPUT
}
```

For comparison, we have also evaluated GPT-3.5 and GPT-4 on the same examples using LangChain's [OpenAI-specific agent](https://github.com/langchain-ai/langchain/tree/021b0484a8d9e8cf0c84bc164fb904202b9e4736/libs/langchain/langchain/agents/openai_functions_agent).
Since this uses their own function-calling template, on which they were fine-tuned, this means the OpenAI models should be at their top performance.

### Results

Since the open-source models were not specifically fine-tuned for calling functions in the given output format, they are at a slight disadvantage compared to the OpenAI agents.

Despite this, some models perform really well! 💪

Here’s an example of Mixtral-8x7B answering the question: `“Which city has a larger population, Guiyang or Tacheng?”`


```markdown
Thought: To answer this question, I need to find the current populations of both Guiyang and Tacheng. I will use the search tool to find this information.
Action:
{
    "action": "search",
    "action_input": "current population of Guiyang"
}
4.697 million (2016)

Thought: I have obtained the population of Guiyang, which is 4.697 million (as of 2016). Now, I will use the search tool again to find the population of Tacheng.
Action:
{
    "action": "search",
    "action_input": "current population of Tacheng"
}
Population: Xinjiang: Tacheng data was reported at 1,110.000 Persons in 2021. This records a decrease from the previous number of 1,138.638 Persons for 2020.
Population: Xinjiang: Tacheng data is updated yearly, averaging 1,023.000 Persons from Dec 2005 to 2021, with 17 observations.

I have obtained the population of Tacheng, which is approximately 1.11 million (as of 2021). Comparing the two populations, Guiyang has a larger population than Tacheng.

Thought: I now know the final answer
Final Answer: Guiyang has a larger population, which is approximately 4.697 million (as of 2016), compared to Tacheng's population of approximately 1.11 million (as of 2021).
```

Here is a benchmark of the models on our evaluation dataset (the average scores originally on a scale of 1-5 have been converted to a scale of 0-100% for readability):

<p align="center">
    <img src="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/open-source-llms-as-agents/benchmark_agents.png" alt="benchmark of agents performance" width="90%">
</p>

As you can see, some open-source models do not perform well in powering agent workflows: while this was expected for the small Zephyr-7b, Llama2-70b performs surprisingly poorly.

👉 But **Mixtral-8x7B performs really well: it even beats GPT-3.5!** 🏆

And this is out-of-the-box performance: ***contrary to GPT-3.5, Mixtral was not finetuned for agent workflows*** (to our knowledge), which somewhat hinders its performance. For instance, on GAIA, 10% of questions fail because Mixtral tries to call a tool with incorrectly formatted arguments. **With proper fine-tuning for the function calling and task planning skills, Mixtral’s score would likely be even higher.**

➡️ We strongly recommend open-source builders to start fine-tuning Mixtral for agents, to surpass the next challenger: GPT-4! 🚀

**Closing remarks:**

- The GAIA benchmark, although it is tried here on a small subsample of questions and a few tools, seems like a very robust indicator of overall model performance for agent workflows, since it generally involves several reasoning steps and rigorous logic.
- The agent workflows allow LLMs to increase performance: for instance, on GSM8K, [GPT-4’s technical report](https://arxiv.org/pdf/2303.08774.pdf) reports 92% for 5-shot CoT prompting: giving it a calculator allows us to reach 95% in zero-shot . For Mixtral-8x7B, the [LLM Leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard) reports 57.6% with 5-shot, we get 73% in zero-shot. _(Keep in mind that we tested only 20 questions of GSM8K)_
