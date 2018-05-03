[官网安装教程](http://caffe.berkeleyvision.org/install_apt.html)

先不要安装虚拟环境
```
 conda create -n caffe python=3.5
 
 conda activate caffe
 
 conda deactivate
```


需要保证添加了cuda路径和安装了cudnn

```
sudo gedit ~/.bashrc
export LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH 

```


查看cuda版本对不对， 系统更新时可能会把cuda给更新了。以后不要随便更新系统文件了


```
cuda 版本 
cat /usr/local/cuda/version.txt

cudnn 版本 
cat /usr/local/cuda/include/cudnn.h | grep CUDNN_MAJOR -A 2
```

## 方法1（注意先把conda的源改成清华镜像）：
```
conda install caffe
```

## 方法2：（在系统环境下安装可行，中间遇到什么问题再搜对应的错误信息和解决方案即可）

 [参考中文安装教程1](https://blog.csdn.net/yhaolpz/article/details/71375762)
 
 [参考中文安装教程2](http://yingshu.ink/2017/01/12/Python3-5-Anaconda3-Caffe%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA/) ， 更改Makefile config文件的方法。
 
 [参考中文安装教程3](https://blog.csdn.net/liu941027/article/details/78106462)
 
 [参考中文安装教程4](https://blog.csdn.net/xiongchao99/article/details/79099173)

 
 注意： 1）第9步和第10部那里make时不要sudo权限
       2） make前把python环境改为系统的默认环境
       暂时办法
       
       
  ```
  sudo rm /usr/bin/python
  sudo ln -s /usr/bin/python2.7 /usr/bin/python
  PATH=/usr/bin:$PATH
 ```
        
 永久修改
 ```
sudo gedit ~/.bashrc

## 添加
alias python=/usr/bin/python

##立即生效
source ~/.bashrc

 ```
        
 * ImportError: dynamic module does not define module export function (PyInit__caffe)
 
[python 版本不能太高](https://stackoverflow.com/questions/34295136/importerror-dynamic-module-does-not-define-module-export-function-pyinit-caff)

 
* m//home/yali/anaconda2/lib/libpng16.so.16：对‘inflateValidate@ZLIB_1.2.9’未定义的引用

[解决办法1](https://blog.csdn.net/ruotianxia/article/details/78437464)

[如果办法1不行](https://stackoverflow.com/questions/48306849/lib-x86-64-linux-gnu-libz-so-1-version-zlib-1-2-9-not-found)

* /sbin/ldconfig.real: /usr/local/cuda-8.0/lib64/libcudnn.so.5 

[解决办法](https://blog.csdn.net/m0_37407756/article/details/70789271)， 如果不行关掉终端重新打开编译

* 关于训练caffe模型出现./build/tools/caffe: command not found

[解决办法](https://blog.csdn.net/xunan003/article/details/72997028)

* This program requires version 3.2.0 of the Protocol Buffer runtime library, but the installed version is 2.6.1

https://www.cnblogs.com/mengmengmiaomiao/p/8134771.html




## 方法3： 虚拟环境下安装caffe， 参考这个教程装(有bug没解决)

https://yangcha.github.io/Caffe-Conda3/

## 在终端可以import caffe但是在pycharm中No module named caffe

```
import sys
sys.path.append("/home/ml/caffe/python")
```

如果太长了没有答案，就把核心的错误拿来搜索
比如 * ImportError: /home/ml/anaconda3/lib/./libharfbuzz.so.0: undefined symbol: FT_Get_Var_Blend_Coordinates

https://www.cnblogs.com/haoliuhust/p/7738920.html

首先，参照这个教程安装HarfBuzz: http://www.linuxfromscratch.org/blfs/view/svn/general/harfbuzz.html,
然后参照这个教程安装bZip2,注意加  -fPIC， ，没有./configure,直接
```
make 
sudo make install
```
然后参照这个教程安装freetype：https://blog.csdn.net/dongtinghong/article/details/72731156， 以及官方说的装两次
http://www.linuxfromscratch.org/blfs/view/svn/general/freetype2.html

然后重启

接着会遇到这个问题：




#### 自己的教程

1、 首先需要安装依赖项目
```
sudo apt-get install libprotobuf-dev libleveldb-dev libsnappy-dev libopencv-dev libhdf5-serial-dev protobuf-compiler

sudo apt-get install --no-install-recommends libboost-all-dev

sudo apt-get install libopenblas-dev liblapack-dev libatlas-base-dev

sudo apt-get install libgflags-dev libgoogle-glog-dev liblmdb-dev

sudo apt-get install git cmake build-essential
```

2、确保nvidia driver， cuda8 ， cudnn 5安装好了


3、编译caffe
  3.1 修改Makefile文件[参考中文安装教程2](http://yingshu.ink/2017/01/12/Python3-5-Anaconda3-Caffe%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA/) ， 更改Makefile config文件的方法。

