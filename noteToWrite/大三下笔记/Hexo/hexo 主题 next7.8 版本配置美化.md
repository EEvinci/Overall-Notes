# hexo 主题 next7.8 版本配置美化

[TOC]

# 设置博主文字描述和中文语言

## 站点配置文件修改 site

```
copytitle: Kali
subtitle: IT博客
description: 没有目的，就做不成任何事情
keywords:
author: KaliAlbert
language: zh-CN
timezone: Asia/Shanghai
```



------

# 设置 next 主题和主题样式

站点配置文件

```
copytheme: next
```

主题配置文件

```
copy#Schemes
#scheme: Muse
#scheme: Mist
#scheme: Pisces
scheme: Gemini
```

------

# 设置首页不显示全文

主题配置文件修改：

```
copyexcerpt accurately.
auto_excerpt:
enable: true
length: 150
```

------

# 设置博客文章持久化连接

## 安装 hexo-abbrlink 这个插件

```
copynpm install hexo-abbrlink --save
```

## 站点配置文件修改 permalink 添加如下内容

```
copypermalink: post/:abbrlink.html
abbrlink:
  alg: crc32  
  rep: hex
```

------

# Menu 增加关于、标签、分类页面

## 站点配置文件修改 menu

将 about、tags、categories 前的 #号去掉，示例如下：

```
copymenu:
  home: / || fa fa-home
  about: /about/ || fa fa-user
  tags: /tags/ || fa fa-tags
  categories: /categories/ || fa fa-th
```

## 新建相关页面

```
copyhexo new page "about"
hexo new page "tags"
hexo new page "categories"
```

## 修改生成页面的配置

source\about\index.md
source\tags\index.md
source\categories\index.md

```
copy---
title: 关于
type: "about"
---
---
title: 标签
type: "tags"
---
---
title: 分类
type: "categories"
---
```

------

# 添加搜索功能

## 安装 exo-generator-searchdb 这个插件

```
copynpm install hexo-generator-searchdb --save
```

## 站点配置文件添加并修改 local_search

```
copysearch:
  path: search.xml
  field: post
  format: html
  limit: 10000
local_search:
  enable: true
```

------

# 设置背景图片和透明度

## 修改主题配置文件中的 custom_file_path

```
copycustom_file_path:
  #head: source/_data/head.swig
  #header: source/_data/header.swig
  #sidebar: source/_data/sidebar.swig
  #postMeta: source/_data/post-meta.swig
  #postBodyEnd: source/_data/post-body-end.swig
  #footer: source/_data/footer.swig
  #bodyEnd: source/_data/body-end.swig
  #variable: source/_data/variables.styl
  #mixin: source/_data/mixins.styl
  style: source/_data/styles.styl
```

## 在博客主站目录下的 source 文件夹下新建_data 文件夹并添加 styles.styl 文件

## 在 styles.styl 中添加如下内容

url 中可以添加本地图片资源
在 next 主题的 source 中新建 assets 目录图片资源放在其中

```
copybody {
    background:url(/assets/background.jpg);
    background-repeat: no-repeat;
    background-attachment:fixed;
    background-position:50% 50%;
    opacity: 0.8;
    //可选
    +mobile(){
      //background-position: 0% -20%;https://i.loli.net/2018/12/29/5c270a0523154.jpg
      //https://i.loli.net/2018/12/29/5c270fc2bfcad.png
      background-image: url(https://ziyuan.lruihao.cn/images/bg_cell.png);
      background-size: cover;
    }
}
```

------

# 设置 canvas_ribbon 动态背景

## 进入到 NexT 主题目录下

## 安装模块到 source/lib 目录下

```
copygit clone https://github.com/theme-next/theme-next-canvas-ribbon source/lib/canvas-ribbon
```

## 编辑主题配置文件，启用 canvas_ribbon 模块，如下：

```
copycanvas_ribbon:
  enable: true
  size: 300
  alpha: 0.6
  zIndex: -1
```

------

# 设置左上角或右上角 github 图标

主题配置文件，启用 github-banner 如下：

```
copygithub_banner:
  enable: true
  permalink: https://https://github.com/KaliAlbert
  title: Follow me on GitHub
```

------

# 设置侧栏阅读进度百分比

编辑站点配置文件，修改 back2top 部分如下

```
copyback2top:
  enable: true
  sidebar: true
  scrollpercent: true
```

------

# 设置阅读位置标记功能

## 进入到 NexT 主题目录下

## 安装模块到 source/lib 目录下：

```
copygit clone https://github.com/theme-next/theme-next-bookmark.git source/lib/bookmark
```

## 编辑主题配置文件，启用 bookmark 模块，如下：

```
copybookmark:
  enable: true
  save: auto
```

------

# 设置字数统计和预计阅读时间

## 进入到博客主站目录下，安装 Hexo 插件：

```
copynpm install hexo-symbols-count-time --save
```

## 编辑站点配置文件，添加如下内容：

```
copysymbols_count_time:
  symbols: true 
  time: true 
  total_symbols: true 
  total_time: true
```

## 此插件集成在 NexT 主题中，在 Hexo 站点配置文件中启用插件后，你可以调整 NexT 配置中的选项，查看主题配置文件，配置如下：

```
copysymbols_count_time:
  separated_meta: true 
  item_text_post: true 
  item_text_total: true 
  awl: 2
  wpm: 275
```

------

# 添加文章分享按钮

## 进入到 NexT 主题目录下

## 安装模块到 source/lib 目录下：

```
copygit clone https://github.com/theme-next/theme-next-needmoreshare2 source/lib/needsharebutton
```

## 编辑主题配置文件，添加 needmoreshare2 模块，如下：

```
copyneedmoreshare2:
  enable: true
  postbottom:
    enable: true
    options:
      iconStyle: default
      boxForm: horizontal
      position: bottomCenter
      networks: Weibo,Wechat,Douban,QQZone
  float:
    enable: false
    options:
      iconStyle: default
      boxForm: horizontal
      position: middleRight
      networks: Weibo,Wechat,Douban,QQZone
```

------

# 设置网页底部信息

查看主题配置文件，修改 footer 配置如下：

```
copyzixingguankan
```

------

# 网站底部添加网站运行时间

## 修改主题下 layout_partials\footer.swig，并添加内容如下：

```
copy<!-- 网站运行时间的设置 -->
<span id="timeDate">载入天数...</span>
<span id="times">载入时分秒...</span>  Sometimes your whole life boils down to one insame move.
<script>
    var now = new Date();
    function createtime() {
        var grt= new Date("01/05/2020 00:00:00");//此处修改你的建站时间或者网站上线时间
        now.setTime(now.getTime()+250);
        days = (now - grt ) / 1000 / 60 / 60 / 24; dnum = Math.floor(days);
        hours = (now - grt ) / 1000 / 60 / 60 - (24 * dnum); hnum = Math.floor(hours);
        if(String(hnum).length ==1 ){hnum = "0" + hnum;} minutes = (now - grt ) / 1000 /60 - (24 * 60 * dnum) - (60 * hnum);
        mnum = Math.floor(minutes); if(String(mnum).length ==1 ){mnum = "0" + mnum;}
        seconds = (now - grt ) / 1000 - (24 * 60 * 60 * dnum) - (60 * 60 * hnum) - (60 * mnum);
        snum = Math.round(seconds); if(String(snum).length ==1 ){snum = "0" + snum;}
        document.getElementById("timeDate").innerHTML = "本站已安全运行 "+dnum+" 天 ";
        document.getElementById("times").innerHTML = hnum + " 小时 " + mnum + " 分 " + snum + " 秒";
}
setInterval("createtime()",250);
</script>
```

------

# 添加自定义 404 页面

```
copyhexo new page 404
```

编辑新建的页面文件，默认在站点根目录下 /source/404/index.md，在 front-matter 中添加 permalink: /404，表示指定该页面固定链接为 http://“主页”/404.html

```
copy---
title: 404
comments: false
permalink: /404
---

<center>404 Not Found
对不起，您所访问的页面不存在或者已删除
[点击此处](https://kalialbert.github.io/)返回首页
</center>

* 我的Github：[https://kalialbert.github.io/](https://kalialbert.github.io/)
```

------

# 添加图片放大预览功能

在主题配置文件，启用 fancybox，修改配置如下：

```
copyfancybox: true
```

------

# 图片懒加载设置

在主题配置文件中启用 lazyload

```
copylazyload: true
```

------

# 点击出现桃心效果 (可选)

## 在主题 /source/js/ 下新建文件 clicklove.js，添加内容如下

```
copy!function(e,t,a){function n(){c(".heart{width: 10px;height: 10px;position: fixed;background: #f00;transform: rotate(45deg);-webkit-transform: rotate(45deg);-moz-transform: rotate(45deg);}.heart:after,.heart:before{content: '';width: inherit;height: inherit;background: inherit;border-radius: 50%;-webkit-border-radius: 50%;-moz-border-radius: 50%;position: fixed;}.heart:after{top: -5px;}.heart:before{left: -5px;}"),o(),r()}function r(){for(var e=0;e<d.length;e++)d[e].alpha<=0?(t.body.removeChild(d[e].el),d.splice(e,1)):(d[e].y--,d[e].scale+=.004,d[e].alpha-=.013,d[e].el.style.cssText="left:"+d[e].x+"px;top:"+d[e].y+"px;opacity:"+d[e].alpha+";transform:scale("+d[e].scale+","+d[e].scale+") rotate(45deg);background:"+d[e].color+";z-index:99999");requestAnimationFrame(r)}function o(){var t="function"==typeof e.onclick&&e.onclick;e.onclick=function(e){t&&t(),i(e)}}function i(e){var a=t.createElement("div");a.className="heart",d.push({el:a,x:e.clientX-5,y:e.clientY-5,scale:1,alpha:1,color:s()}),t.body.appendChild(a)}function c(e){var a=t.createElement("style");a.type="text/css";try{a.appendChild(t.createTextNode(e))}catch(t){a.styleSheet.cssText=e}t.getElementsByTagName("head")[0].appendChild(a)}function s(){return"rgb("+~~(255*Math.random())+","+~~(255*Math.random())+","+~~(255*Math.random())+")"}var d=[];e.requestAnimationFrame=function(){return e.requestAnimationFrame||e.webkitRequestAnimationFrame||e.mozRequestAnimationFrame||e.oRequestAnimationFrame||e.msRequestAnimationFrame||function(e){setTimeout(e,1e3/60)}}(),n()}(window,document);
```

## 修改_layout.swig

在主题 \layout_layout.swig 文件末尾添加：

```
copy<!-- 页面点击小红心 -->
<script type="text/javascript" src="/js/clicklove.js"></script>
```

------

# 主页文章添加置顶图标 (可选)

修改主题的 /layout/_macro/post.swig 文件，在

下加入 “置顶” 标识，如图标和文字描述：



```
copy{% if post.top %}
<i class="fa fa-thumb-tack"></i>
<font color=7D26CD>{{ __('post.sticky') }}</font>
<span class="post-meta-divider">|</span>
{% endif %}
```

------

# 标签云特效（可选）

```
copynpm install hexo-tag-cloud@^2.0.* --save
```

在主题文件夹找到文件 theme/next/layout/_macro/sidebar.swig, 然后在 back2top.sidebar 上方添加如下代码

```
copy{% if site.tags.length > 1 %}
<script type="text/javascript" charset="utf-8" src="/js/tagcloud.js"></script>
<script type="text/javascript" charset="utf-8" src="/js/tagcanvas.js"></script>
<div class="widget-wrap">
    <h3 class="widget-title">Tag Cloud</h3>
    <div id="myCanvasContainer" class="widget tagcloud">
        <canvas width="250" height="250" id="resCanvas" style="width=100%">
            {{ list_tags() }}
        </canvas>
    </div>
</div>
{% endif %}
```

在主站配置文加下添加内容如下

```
copy# hexo-tag-cloud
tag_cloud:
    textFont: Trebuchet MS, Helvetica
    textColor: '#333'
    textHeight: 25
    outlineColor: '#E2E1D1'
    maxSpeed: 0.1
```

------

# 主页文章添加阴影效果

在 source/_data/styles.styl 中添加内容如下

```
copy.post {
   margin-top: 60px;
   margin-bottom: 60px;
   padding: 25px;
   -webkit-box-shadow: 0 0 5px rgba(202, 203, 203, .5);
   -moz-box-shadow: 0 0 5px rgba(202, 203, 204, .5);
}
```

------

# 设置代码块复制和代码高亮

在主题配置文件中修改 codeblock

```
copycodeblock:
  highlight_theme: normal
  copy_button:
    enable: true
    show_result: true
    style:
```

------

# 网站侧栏背景及主副标题颜色

在主站 source/_data/styles.styl 中添加内容如下

```
copy//题头
.site-meta {
    background: $blue; 
}
//主标题颜色
.brand{
    color: #4dfc23
}
//副标题颜色
.site-subtitle{
    color: #4dfc23
}
```

------

# 修改文章内链接文本样式

打开文件 /themes/next/source/css/_common/components/post/post.styl，在末尾添加以下

```
copy.post-body p a{
  color: #0593d3;
  border-bottom: none;
  border-bottom: 1px solid #0593d3;
  &:hover {
    color: #fc6423;
    border-bottom: none;
    border-bottom: 1px solid #fc6423;
  }
}
```

------

# 修改文章底部标签样式

在主题配置文件中修改

```
copytag_icon: true
```

------

# 在文章末尾添加 “文章结束” 标记

在主题 /layout/_macro 下新建 passage-end-tag.swig 文件，并添加以下代码

```
copy<div style="text-align:center;color: #ccc;font-size:14px;">-------------本文结束 <i class="fa fa-heart"></i> 感谢阅读-------------</div>
```

打开 /themes/next/layout/_macro/post.swig 文件，在 END POST BODY 后面引入 passage-end-tag.swig，如下

```
copy{#####################}
{### END POST BODY ###}
{#####################}
{% if theme.passage_end_tag.enable and not is_index %}
{% include 'passage-end-tag.swig' %}
{% endif %}
```

在主题配置文件 _config.yml 的末尾添加以下配置

```
copypassage_end_tag:
  enable: true
```

------

# 修改分类页面样式

在主站 source/_data/styles.styl 中添加内容如下

```
copy// 分类&&标签 页面样式
.post-block.page {
    margin-top: 40px;
}
// 分类页面page
.category-all-page {
    box-shadow: 0px 0px 10px 0px rgba(0, 0, 0, 0.5);
    background-color: #797D7F;
    padding: 20px 30px 60px 30px;
    border-radius: 25px 25px 25px 25px;
}
.category-all-title {
    font-family: Impact;
    font-size: 24px;
    color: aqua;
}
.category-list {
    overflow: auto;
}
.category-list li {
    height: 100%;
    float: left;
    border-right: 3px solid #222;
    padding: 0 20px;
}
.category-all ul li {
    list-style: none!important;
}
.category-list li:last-child {
    border-right: none;
}
.category-list li a {
    font-size: 16px;
    text-decoration: none;
    color: chartreuse;
    font-family: Helvetica, Verdana, sans-serif;
    // text-transform: uppercase;
    -webkit-transition: all 0.5s ease;
    -moz-transition: all 0.5s ease;
    -o-transition: all 0.5s ease;
    -ms-transition: all 0.5s ease;
    transition: all 0.5s ease;
}
.category-list li a:hover {
    color: black;
}
.category-list li.active a {
    font-weight: bold;
    color: black;
}
```

------

# 设置头像

## 在站点配置文件下修改 avatar

# 网站底部加上访问量

打开主题的配置文件 /theme/next/_config.yml，找到如下配置 busuanzi_count（不蒜子）启用

```
copybusuanzi_count:
  enable: true
```

------

# 修改不蒜子颜色

在主站 source/_data/styles.styl 中添加

```
copy// 修改不蒜子数据颜色
#busuanzi_value_site_pv,#busuanzi_value_site_uv{
  color: #00BFFF;
}
```

------

# 网站底部添加动态桃心

修改主题配置文件中 icon

```
copyicon:
    name: fa fa-heart 
    animated: true 
    color: "#ff0000"
```

------

# 网站底部添加备案信息 (可选)

在主题 \layout_partials\footer.swing 下添加

```
copy<div class="BbeiAn-info" style="color:#4dfc23">
    {{ __('鄂ICP备') }} -
    <a target="_blank" href="http://www.miitbeian.gov.cn/" style="color:#4dfc23;"  rel="nofollow">18025394</a> <!--a标签中增加nofollow属性，避免爬虫出站。-->| 
    <a target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=42090202000295" style="text-decoration:none;color:#4dfc23;padding-left:30px;background:url(https://s1.ax1x.com/2018/09/29/ilmwIH.png) no-repeat left center" rel="nofollow">{{ __('鄂公网安备 42090202000295') }}</a>    <!--这里将图标作为了背景，以使得能和后面的文字在同一行-->
</div>
```

------

# 侧边栏社交链接

修改主题配置文件

```
copysocial:
  GitHub: https://github.com/KaliAlbert || fab fa-github
  E-Mail: 172468103@qq.com || fa fa-envelope
  Bili: https://space.bilibili.com/15071276 || fa fa-tv
```

------

# 添加侧栏友情链接

在主题配置文件中修改 Blog rolls

```
copylinks_settings:
  icon: fa fa-link
  title: Friend Links
  layout: inline
  
links:
  V2EX: https://www.v2ex.com/
  #Title: http://yoursite.com
```

------

# 在文章底部增加版权信息

编辑 主题配置文件，修改如下配置：

```
copycreative_commons:
  license: by-nc-sa
  sidebar: true
  post: true
  language:
```

------

# 关于页面样式的修改，回顶部按钮样式、底部页码等等

在博客主站 \source_data\styles.styl 中添加内容如下

```
copy//TOC目录全部展开
.post-toc.nav.nav-child {
  display: block;
}
//TOC目录不显示三级以上目录
.nav-level-3.nav-child {
  display: none !important;
}

// 右下角返回顶部按钮样式
.back-to-top:hover {
    color: rgb(136, 255, 13);
	background-color: rgba(0, 0, 0, 0.75); //black
}

// 文章代码块顶部样式
.highlight figcaption {
    margin: 0em;
    padding: 0.5em;
    background: #eee;
    border-bottom: 1px solid #e9e9e9;
}
.highlight figcaption a {
    color: rgb(80, 115, 184);
}

//代码块复制按钮
.highlight{
  //方便copy代码按钮（btn-copy）的定位
  position: relative;
}
.btn-copy {
    display: inline-block;
    cursor: pointer;
    background-color: #eee;
    background-image: linear-gradient(#fcfcfc,#eee);
    border: 1px solid #d5d5d5;
    border-radius: 3px;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    -webkit-appearance: none;
    font-size: 13px;
    font-weight: 700;
    line-height: 20px;
    color: #333;
    -webkit-transition: opacity .3s ease-in-out;
    -o-transition: opacity .3s ease-in-out;
    transition: opacity .3s ease-in-out;
    padding: 2px 6px;
    position: absolute;
    right: 5px;
    top: 5px;
    opacity: 0;
}
.btn-copy span {
    margin-left: 5px;
}
.highlight:hover .btn-copy{
  opacity: 1;
}

//修改文章内code样式
code {color:#c7254e;background:#f9f2f4;border:1px solid #d6d6d6;}

// [Read More]按钮样式: 黑底绿字
.post-button .btn:hover {
	
    color: rgb(136, 255, 13) !important;
	background-color: rgba(0, 0, 0, 0.75); //black
}

// 页面底部页码
.pagination .page-number.current {
	
    border-radius: 100%;
    background-color: rgba(100, 100, 100, 0.75);
}
// 页面底部页码, 去除鼠标置于上方时，数字上方的线
.pagination .prev, .pagination .next, .pagination .page-number {
    margin-bottom: 10px;
    border: none;
	color: rgb(1, 1, 1);
}

// 页面底部页码，鼠标置于上方，黑底绿字
.page-number:hover,.page-number:active{
	color: rgb(136, 255, 13);
	border-radius: 100%;
    //background-color: rgba(255, 0, 100, 0.75); //品红
	background-color: rgba(0, 0, 0, 0.75); //black
}
```

