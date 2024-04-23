
[TOC]

## 部署hexo

先安装nodejs，不然没法使用npm

```
# 全局安装hexo
npm install -g hexo-cli
# 创建并初始化hexo文件夹
hexo init <文件夹>
# 进入创建好的目录
cd <文件夹> 
# 使用npm安装相关依赖
npm install
```



## 界面美化

### 配置和安装主题

根据需求配置`_config.yml`文件，参考：

> https://hexo.io/docs/configuration

安装主题，我这里用的是`next`：

> https://github.com/next-theme/hexo-theme-next
>
> ```
> $ cd hexo-site
> $ git clone https://github.com/next-theme/hexo-theme-next themes/next
> ```
>
> 根据上面的链接配置完成后，可以使用`hexo server`命令启动本地服务，验证是否配置成功。

### 注意！

注意，如果安装了next主题，并且想修改相关配置，请将`blog\themes\next`目录中的`_config.yml`文件拷贝到blog根目录中，并重命名为`_config.next.yml`，然后修改`_config.next.yml`以自定义配置，这一点官方文档有说明，不然主题更新了，可能会导致配置文件被覆盖。

### 对主题的深度自定义 友情链接

> https://kalialbert.github.io/article/107153072.html

### 新版本添加鼠标特效和背景特效

> 将特效的js代码放入`themes\next\source\js`路径中，名字自定义，我这里加了一个背景和一个点击特效
>
> ![截图](https://byzain.github.io/hexo/f9a2b0874180edb1ecb354f0eb06a5d7.png)
>
> 然后去`themes\next\layout`下去修改layout.njk的配置，引入刚才添加的js：
>
> ![截图](https://byzain.github.io/hexo/d8d57fd41691882116b4d1c4e1d05e63.png)

## 推到github上托管

### 创建github个人首页：

在GitHub上创建个人仓库，仓库名称为`<你的github用户名>.github.io

### 配置config文件

还是去你自己创建的文件夹中找到`_config.yml`文件，在文件的最后，加入 如下内容

repo中是你刚才创建的仓库的git地址

```
deploy:
  type: git
  repo: git@github.com:ByZain/ByZain.github.io.git
  branch: master
```

### 推送

```
hexo g & hexo d
```

## 关于图片无法显示问题

修改配置文件`_config.yml`中`post_asset_folder的`值为`true`：

```
post_asset_folder: true
```

进入博客目录，安装插件：

```
npm install https://github.com/CodeFalling/hexo-asset-image --save
```

配置完成，编写文章：

```
hexo new <title>
```

此时会在`blog\source\_posts`下生成一个`<title>.md`文件以及`<title>`文件夹

这时候只需要将图片放入文件夹中，md中不用加路径，直接引用即可

post文件夹结构：

![截图](https://byzain.github.io/hexo/3799ba45e23c5dc5ee41b6d140eb7065.png)

![截图](https://byzain.github.io/hexo/07f4897ad362840ac92ffb87a3886492.png)

![截图](https://byzain.github.io/hexo/80f59394723baa650e21c5d6ff888c0b.png)

## 很好用的插件

### 文章加密

#### 安装插件

进入blog目录执行命令

```
npm install --save hexo-blog-encrypt
```

#### 全局设置

设置hexo配置文件`_config.yml`，为文章设置同一的默认口令，直接追加到配置文件底部即可

tag中声明了私有标签名，和文章的同一密码，当文章需要加密的时候，为文章添加`private`标签即可

全局中可以声明多个密码和tag的组合，用来为不同类型的文章上锁

```
# Security
encrypt: # hexo-blog-encrypt
  silent: true
  abstract: 这是一篇加密文章，需要密码才能继续阅读。
  message: 当前文章暂不对外可见，请输入密码后查看！
  tags:
  - {name: private, password: hello}
##- {name: private2, password: passwd2} 
  wrong_pass_message: 抱歉，您输入的密码错误，请检查后重新输入。
  wrong_hash_message: 抱歉, 当前文章不能被校验, 不过您还是可以看看解密后的内容。
```

#### 自定义密码

如果文章不想使用全局设置的密码，也可以为其设置自定义密码覆盖掉全局的密码设置，直接在文章中添加`tag`即可，格式如下：

```
tags:
- {name: private, password: hello}
```

或者

```
tags:
    - private
password: "hello"
```

### 评论插件

评论插件用的是`gitalk`，next已经内置了，只需要配置参数即可。

#### 注册github OAuth application

访问https://github.com/settings/applications/new ，相关信息按以下方法填写：

```
Application name： # 应用名称，随意填写即可
Homepage URL： # 你的网站地址，如https://yourname.github.io
Application description # 描述，随意填写即可
Authorization callback URL：# 你的网站地址，如https://yourname.github.io
```

将NexT的`_config.yml`，拷贝到博客根目录，重命名为`_config.next.yml`然后再修改其内容

```
gitalk:
  enable: true # 此处改为true
  github_id: yourname # 修改为的Github账户名，非邮箱地址
  repo: yourname.github.io  # 修改为你的仓库名
  client_id:  # 填入上一步中得到的Client ID
  client_secret:  # 填入上一步中得到的Client Secret
  admin_user: yourname # 修改为的Github账户名，非邮箱地址
  proxy: https://cors-anywhere.azm.workers.dev/https://github.com/login/oauth/access_token/
  distraction_free_mode: false # 此处为false
  # Gitalk's display language depends on user's browser or system environment
  # If you want everyone visiting your site to see a uniform language, you can set a force language value
  # Available values: en | es-ES | fr | ru | zh-CN | zh-TW
  language: zh-CN #语言设为中文
```

## hexo相关命令

生成静态文件

```
hexo generate # 可以缩写为 hexo g
```

部署网站

```
hexo deploy # 可以简写为 hexo d
```

启动服务

```
hexo server
# -p 指定端口
# -s 只使用静态文件
```

清除缓存和已经生成的静态文件

```
hexo clean
```

列出网站资料

```
hexo list <type>
```

安全模式

```
hexo --safe # 不载入插件和脚本
```

推荐使用：

```
hexo clean && hexo g && hexo s
```

## 整站源码备份和恢复

### 备份

将整站源码上传至GitHub，记得删除主题目录下的`.git`文件，否则主题不会被上传，另外根目录下也有类似`.git`的文件会阻止部分源码上传，可以直接删除。

### 恢复

git拉取下来之后需要安装`hexo-deployer-git`，删除`.deploy_git`文件夹后即可正常部署，否则无法部署

> npm install hexo-deployer-git –save

另外如果配置了站点地图，迁移的时候同样需要重新安装

> npm install hexo-generator-sitemap –save

[# blog搭建](https://byzain.github.io/tags/blog搭建/)

[ htaccess文件的深入学习](https://byzain.github.io/htaccess文件的深入学习/)

[cobaltstrike中文乱码解决 ](https://byzain.github.io/cobaltstrike中文乱码解决/)

[0](https://github.com/ByZain/ByZain.github.io/issues/35) 条评论

EEvinci

![@EEvinci](https://avatars.githubusercontent.com/u/93924805?v=4)

[支持 Markdown 语法](https://guides.github.com/features/mastering-markdown/)评论预览

来做第一个留言的人吧！

© 2022 Zain

 4230  5423

由 [Hexo](https://hexo.io/) & [NexT.Muse](https://theme-next.js.org/muse/) **强力驱动**