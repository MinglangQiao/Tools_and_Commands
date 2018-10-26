[官网](http://pytorch.org/)

### 首先把[清华镜像](https://mirror.tuna.tsinghua.edu.cn/help/anaconda/)加入conda的源文件, 速度飞快，可以避免cudatoolkit安装失败导致no module name torch等问题


选择合适的版本，then
```
conda install pytorch torchvision -c pytorch
```

如果出现了[jupyter notebook在pycharm中不能正常使用](http://zhuangzhuang.github.io/2017/01/22/fix-pycharm-jupyter/)


### 2 pytorch 使用visdom
[github主页](https://github.com/facebookresearch/visdom)

[知乎1](https://zhuanlan.zhihu.com/p/34692106)


###关于.data 和 .detach
https://github.com/pytorch/pytorch/issues/6990

.data时，如果对x.data进行了赋值等inplcae的操作，不会被autograd追踪，所以在反向传播的时候，算x处的梯度时，网络会把当前的x值直接带入计算梯度，但实际上x
的值是被x.data的操作改变的，而不是被网络训练改变的，所以不能直接把这个由于外来操作改变了的x值用来算梯度，这样就会有错

.detach 就会记录这些操作，在你算梯度的时候报错，提醒你x.detach被has been modified by an inplace operation， 这是正确的

在拷贝参数时用下.data没问题，因为本来就是在这些训练好的参数上继续训练，直接用这些值算参数，不需要考虑以前的操作

在算loss时也没影响，因为下一个out是重新计算得到的，下一轮的out和上一轮的out没关系
