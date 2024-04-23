# 动量法（Momentum）

**是传统的SGD算法的扩展，比SGD算法更加高效**

记录梯度的增量并于当前的梯度相加得到

![image-20240106162745607](https://evinci.oss-cn-hangzhou.aliyuncs.com/img/image-20240106162745607.png)

β1有一个经验值0.9

即更多的依靠过去积累的动量，再加上当前梯度的0.1倍，类似于惯性的感觉

梯度更多的记录之前的信息，即梯度的波动会减弱

![image-20240106163043429](https://evinci.oss-cn-hangzhou.aliyuncs.com/img/image-20240106163043429.png)