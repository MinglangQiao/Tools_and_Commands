## 最快最简单的办法，20+ M/S, 用清华镜像， [安装网址](https://mirrors.tuna.tsinghua.edu.cn/help/tensorflow/)，选择版本，一键安装
```
pip install \
  -i https://pypi.tuna.tsinghua.edu.cn/simple/ \
  https://mirrors.tuna.tsinghua.edu.cn/tensorflow/linux/gpu/tensorflow_gpu-1.0.0-cp35-cp35m-linux_x86_64.whl
```

0、选择支持cuda 8.0的版本， 否者报错，
ImportError: libcublas.so.9.0 [解决办法](https://blog.csdn.net/w5688414/article/details/79187499)
```
pip install tensorflow-gpu==1.4  
```

1、[安装问题: wheel 不支持，换个python版本](https://stackoverflow.com/questions/37425579/cannot-install-tensorflow-on-fresh-ubuntu-partition-tensorflow-0-8-0-cp34-cp34m)


2、[ReadTimeoutError报错](https://www.cnblogs.com/xuchenCN/p/5888648.html)

3、### 报错 could not find cudnnCreate in cudnn DSO， 注意查看报错信息
[解决： 把cudnn 版本恢复到V5.1, 对应自己的cuda 版本](https://github.com/tensorflow/tensorflow/issues/722)
[怎样改cudnn版本](https://blog.csdn.net/l297969586/article/details/67632608)
