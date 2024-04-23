# linux服务器连接github

## 创建ssh秘钥

使用`ssh-keygen`生成密钥

`-t`表示生成的密钥的类型，通常生成`rsa`类型的秘钥

`-b`表示生成的密钥的长度，通常使用`2048`或`4096`

`-f`表示指定密钥对文件生成的位置，Linux下通常生成到``/.ssh/my_key`，`my_key`表示秘钥对文件的名字，可以根据情况自行修改

例如，我要创建一个连接github的ssh密钥对，该密钥对只用于连接github，不用于其他网站的ssh服务：

```shell
ssh-keygen -t rsa -b 4096 -f ~/.ssh/github_key
```

### 密钥对可不止一个

如果没有指定秘钥对文件的名称，同时在已经有了密钥对文件的基础上又生成了密钥对文件，那么不要担心~

不会被覆盖！

如果密钥对文件已经存在，`ssh-keygen` 将会在文件名后面附加一个数字来生成唯一的文件名，例如 `id_rsa` 可能会变为 `id_rsa_2`，`id_rsa.pub` 可能会变为 `id_rsa_2.pub`。

这样做是为了避免意外覆盖现有的密钥对文件。通过保留旧的密钥对文件，你可以继续使用现有的公钥进行连接，或者在需要的时候手动切换到新的密钥对。

## 将公钥放到github

使用`cat`/ `more`查看`github_key.pub`，然后复制到github进行连接

```shell
cat ~/.ssh/id_rsa.pub
```

- 登录到 GitHub 帐户，点击右上角的头像，选择 "Settings"（设置）。
- 在左侧导航栏中，选择 "SSH and GPG keys"（SSH 和 GPG 密钥）。
- 点击 "New SSH key"（新建 SSH 密钥）按钮。
- 在 "Title"（标题）字段中，为该密钥提供一个描述性名称。
- 将你从上一步复制的公钥内容粘贴到 "Key"（密钥）字段。
- 最后，点击 "Add SSH key"（添加 SSH 密钥）按钮。

## 输入`ssh -T git@github.com`

验证连接

出现

`Hi ~~！You've successfully authenticated, but GitHub does not provide shell access.`即可