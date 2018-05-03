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

2 确保nvidia driver， cuda8 ， cudnn 5安装好了

3 安装opencv3.1， 从源码安装， [参考](https://github.com/MinglangQiao/Tools_and_Commands/blob/master/Tools/Opencv.md)



4 编译caffe
  4.1 修改Makefile文件[参考中文安装教程2](http://yingshu.ink/2017/01/12/Python3-5-Anaconda3-Caffe%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA/) ， 更改Makefile config文件的方法。


5 如果编译都通过了，import caffe的时候报这个错

```
ImportError: /home/ml/caffe-master/python/caffe/_caffe.so: undefined symbol: PyCObject_Type
```

没有现成的方案， 根据[这个](https://stackoverflow.com/questions/29080596/undefined-symbol-when-importing-f2py-module-using-python-3), 猜测应该是编译的地方与python相关的地方出了问题。 然后根据[这个](https://github.com/BVLC/caffe/issues/489),  关掉shell，重新打开， 然后

```
make clean 
export CPLUS_INCLUDE_PATH=/usr/include/python3.5
```
然后再重新编译

# 注意啦
##########################################################################################
                            正儿八经自己配成功了的教程
###########################################################################################
#### 配置：
Ubuntu16.04 + gtx1080ti + cuda8.0 + cudnn5.1 + opencv3.4 + Anaconda3 + python3.5 + caffe

特别鸣谢一下这几个教程，每个教程都不完全正确（for me），但相互补充，要配合着看： 

 [1 Ubuntu16.04 Caffe 安装步骤记录（超详尽）](https://blog.csdn.net/yhaolpz/article/details/71375762)
 
 [2 Python3.5 Anaconda3 Caffe深度学习框架搭建](http://yingshu.ink/2017/01/12/Python3-5-Anaconda3-Caffe%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E6%A1%86%E6%9E%B6%E6%90%AD%E5%BB%BA/) ， 更改Makefile config文件的方法。
 
 [3 心酸的Caffe安装之路](https://blog.csdn.net/liu941027/article/details/78106462)
 
 [4 ubuntu16.04下，安装caffe+cuda8.0+Anaconda3+cudnn5.1](https://blog.csdn.net/xiongchao99/article/details/79099173)
 
 分为以下4个大步骤：
 
 * 1 安装依赖包
 
 * 2 安装显卡驱动 + cuda8 + cudnn5
 
 * 3 安装 opencv3.4
 
 * 4 ananconda3配置
 
 * 5 安装caffe
 
 安装心得：
 
 * 保证每一步做正确了再做下一步， 如果前面做的不对， 后边可能出现很多意想不到的错误， 错到你怀疑人生
 
 * 遇到什么错就相应的在百度和google搜索; 如果没有现成的答案， 需要合理的推理和参考， 考虑可能的原因并验证
 
 * 实在卡在某个地方动不了了不要死磕， 从头在来一遍， 不要怕麻烦
 
 ## 1 安装依赖包
 ```
 sudo apt-get install libprotobuf-dev libleveldb-dev libsnappy-dev libopencv-dev libhdf5-serial-dev protobuf-compiler

sudo apt-get install --no-install-recommends libboost-all-dev

sudo apt-get install libopenblas-dev liblapack-dev libatlas-base-dev

sudo apt-get install libgflags-dev libgoogle-glog-dev liblmdb-dev

sudo apt-get install git cmake build-essential
 ```
 
 ## 2 安装显卡驱动 + cuda8 + cudnn5
  
### 2.1 安装显卡驱动

 参考[这个教程](https://github.com/MinglangQiao/Tools_and_Commands) 安装显卡驱动， 建议下载NVIDIA的sh文件安装， 最后验证
 
 ```
nvidia-smi
```
  
 ### 2.1 安装cuda
 
 还是参考[这个教程](https://github.com/MinglangQiao/Tools_and_Commands) 安装cuda8.0， 还是建议下载sh文件安装， 最后按教程里面的方法验证

 
```
cd /home/ml/NVIDIA_CUDA-8.0_Samples/1_Utilities/deviceQuery (note: change to your path)
sudo make
./deviceQuery
```

### 2.2 安装cuda

还是参考[这个教程](https://github.com/MinglangQiao/Tools_and_Commands) 安装cudnn5.1，一定要记得按教程里面的sudo ldconfig更新链接
 
 
 ## 3 安装opencv3.4.0
 
 参考[这个教程](https://github.com/MinglangQiao/Tools_and_Commands)的方法2 安装， 即从源码安装，安装完查看opencv版本是否为3.4.0
 
 ## 4 ananconda3配置
 
 * 首先不要在虚拟环境环境下安装caffe， 反正我是没有试成功
 
 * ananconda3的默认python环境是python3.6, 但为了保险我没用默认的python3.6环境，而是新建了一个python=3.5的环境。如果你在默认环境下python = 3.6配成功了，记得告诉我啊
 
 
 ## 5 安装caffe
 
 ### 5.1 更改配置文件(非常关键)
 
 加入解压后的caffe目录，首先创建一个Makefile.config
 ```
 cp Makefile.config.example Makefile.config
 ```
 
 #### 修改Makefile.config文件
 ```
 sudo gedit Makefile.config
 ```
 
 然后修改一下这些配置， 修改后的Makefile.config 和 Makefile已经上传到[这里]()
 * 1 USE_CUDNN=1 #去掉前面的注释
 
 * 2 OPENCV_VERSION=3 #去掉前面的注释，我们使用的是opencv3
 
 * 3 把系统的python环境禁用掉
 ```
# PYTHON_INCLUDE := /usr/include/python2.7 \
# 		/usr/lib/python2.7/dist-packages/numpy/core/include
 ```
 
 * 4 启用ananconda的python3.5环境， 注意ANACONDA_HOME := $(HOME)/anaconda3/envs/python35， 而不是默认的ANACONDA_HOME := $(HOME)/anaconda， 我刚开始以为怎样不行， 结果居然可以
 
 ```
 # Anaconda Python distribution is quite popular. Include path:
# Verify anaconda location, sometimes it's in root.
ANACONDA_HOME := $(HOME)/anaconda3/envs/python35
PYTHON_INCLUDE := $(ANACONDA_HOME)/include \
		# $(ANACONDA_HOME)/include/python3.5m \
		# $(ANACONDA_HOME)/lib/python3.5/site-packages/numpy/core/include
 ```
 
  * 5 PYTHON_LIBRARIES 设置，这里也比较关键
  
 ```
# Uncomment to use Python 3 (default is Python 2)
PYTHON_LIBRARIES := boost_python-py35 python3.5m  
# PYTHON_INCLUDE := /usr/include/python3.5m \
#                 /usr/lib/python3.5/dist-packages/numpy/core/include
```
  
  原文是boost_python3  python3.5m，编译会出找不到文件的错误，从stackflow上面得知有一个解决方法
  ```
  sudo locate boost_python
  ```
  这里是查找自己系统的lboost-python对应的版本，我电脑上的是35,所以将 boost_python3改为 boost_python-py35就可以
  ，如下图所示
  
  
  * 6 INCLUDE_DIRS 和 LIBRARY_DIRS
  ```
INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/local/include
LIBRARY_DIRS := $(PYTHON_LIB) /usr/local/lib /usr/lib 
修改为： 
INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/local/include /usr/include/hdf5/serial
LIBRARY_DIRS := $(PYTHON_LIB) /usr/local/lib /usr/lib /usr/lib/x86_64-linux-gnu /usr/lib/x86_64-linux-gnu/hdf5/serial 
  ```
  
  * 7 启用 WITH_PYTHON_LAYER
  ```
 # Uncomment to support layers written in Python (will link against Python libs)
WITH_PYTHON_LAYER := 1 #因为我就是要用Python来写
 ```
  
  
  * 8 启用 PYTHON_LIB
  ```
  PYTHON_LIB := $(ANACONDA_HOME)/lib
  ```
  
 
 
 #### 修改Makefie文件
 ```
 sudo gedit Makefile
 ```
 
  * 1 修改成下面这样
  ```
将：
LIBRARIES += glog gflags protobuf boost_system boost_filesystem m hdf5_hl hdf5
改为：
LIBRARIES += glog gflags protobuf boost_system boost_filesystem m hdf5_serial_hl hdf5_serial
  ```
  
  * 2 
  ```
  将：
NVCCFLAGS +=-ccbin=$(CXX) -Xcompiler-fPIC $(COMMON_FLAGS)
替换为：
NVCCFLAGS += -D_FORCE_INLINES -ccbin=$(CXX) -Xcompiler -fPIC $(COMMON_FLAGS)
  ```
  
  * 3 修改 /usr/local/cuda/include/host_config.h 文件
```
将
#error-- unsupported GNU version! gcc versions later than 4.9 are not supported!
改为
//#error-- unsupported GNU version! gcc versions later than 4.9 are not supported!
```
 
 ### 5.2 编译caffe
 
  * step 1
  ```
  make all -j12
  ```
如果这一步报了一个这种错
```
In file included from /usr/include/boost/python/detail/prefix.hpp:13:0,
                 from /usr/include/boost/python/args.hpp:8,
                 from /usr/include/boost/python.hpp:11,
                 from python/caffe/_caffe.cpp:8:
/usr/include/boost/python/detail/wrap_python.hpp:50:23: fatal error: pyconfig.h: No such file or directory
```
这么解决

```
make clean 
export CPLUS_INCLUDE_PATH=/usr/include/python3.5
```
然后再编译

* step 2
```
make test -j12
make runtest -j12
make pycaffe -j $(($(nproc) + 1))
```

* step3 添加环境变量
```
sudo vim ~/.bashrc

## 在末尾加入
export PYTHONPATH=/home/ubuntu/caffe/caffe-master/python:$PYTHONPATH

## 立即生效
source ~./bashrc
```

然后
```
cd caffe-master/python/

python

import caffe

```
或者
```
caffe-master/python/python

import caffe
```
写程序时如果报错没有caffe， 需要在开头加入路径
```
```




