# 进入Linux需要查看的几条基本命令

## 查看该系统的Linux具体发行版

```shell
cat /etc/os-release
```

在输出的`name`项中查看系统版本

## 查看该系统使用的shell

```shell
echo $SHELL 
```
其中`SHELL`一定要大写

## 查看该Linux发行版使用的Linux Kernel

```shell
uname -r
```

## 查看使用的shell的版本_以bash为例

```shell
bash --vesion
```

## 查看系统架构(64位还是32位)

```shell
uname -m
```

