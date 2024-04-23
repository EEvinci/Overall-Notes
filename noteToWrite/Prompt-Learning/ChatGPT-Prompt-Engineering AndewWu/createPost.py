import os
import openai

os.environ["HTTP_PROXY"] = "127.0.0.1:7890"
os.environ["HTTPS_PROXY"] = "127.0.0.1:7890"

openai.api.key = "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"

def get_connection(prompt, model="gpt-3.5-turbo"):
    message = [{"role":"user", "text":prompt}]
    print("the type of message is:",type(message),"\n")
    response = openai.Completion.create(
        model = model,
        prompt = message,
        temperature = 0.9,
        max_tokens = 100,
        top_p = 1,
        frequency_penalty = 0.0,
        presence_penalty = 0.0,
        stop = ["\n"]
    )