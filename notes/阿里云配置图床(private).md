# 阿里云配置图床(private)

涉及账号密码, 所以不上传

![08dee58d6241aa3ce811e45163ca92c](https://evinci.com/test/08dee58d6241aa3ce811e45163ca92c.png)

## RAM子账号密码

### 账户名：everton

~~~txt
UserPrincipalName,AccessKeyId,AccessKeySecret
everton@evinci.onaliyun.com,LTAI5t87bMAS2QBvFD5nmDLL,qiUFaoIFGXkI5Q2RX7eHrHuBlJLPUl
~~~

### 权限管理

#### 在子账号管理中, 添加`管理对象存储服务(OSS)权限`

![image-20221125111953125](http://evinci.oss-cn-hangzhou.aliyuncs.com/evinci/image-20221125111953125.png)

![image-20221125111737176](http://evinci.oss-cn-hangzhou.aliyuncs.com/evinci/image-20221125111737176.png)

### 在主账号OSS-Bucket设置中, 为子账号添加权限

![image-20221125112049903](http://evinci.oss-cn-hangzhou.aliyuncs.com/evinci/image-20221125112049903.png)



### 替换地址：

http://evinci.oss-cn-hangzhou.aliyuncs.com/evinci/

### 图片原先存放目录地址

E:/Typora/ty_Photo/



### picGO和OSS管理工具的区别

PicGo是 一个用于快速上传图片并获取图片URL 链接的工具

OSS管理工具： OSSbrowser

## 参考文档

[阿里云OSS图床搭建](https://developer.aliyun.com/article/976564)
