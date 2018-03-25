## Anaconda

### 官网
[Anaconda](https://www.anaconda.com/download/#linux)

[Document](https://docs.anaconda.com/anaconda/)

[清华下载镜像](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/)

#### 一键安装
```
bash 下载/Anaconda3-4.0.0-Linux-x86_64.sh
```

安装完后检验：
```
conda --version
```
如果提示 conda conmand not fond， 则需要添加环境变量
###### 将anaconda的bin目录加入PATH，根据版本不同，也可能是~/anaconda3/bin
```
echo 'export PATH="~/anaconda2/bin:$PATH"' >> ~/.bashrc
```
###### 更新bashrc以立即生效
```
source ~/.bashrc
```

参考[conda修改镜像](http://python.jobbole.com/86236/)再安装环境，速度更快

#### 教程：

#### 简介， 包管理和python环境管理
http://python.jobbole.com/87522/

##### 设置Anaconda镜像
http://python.jobbole.com/86236/

### Conda的环境管理

##### 创建虚拟环境
```
conda create -n env_name  list of packages

# 安装好后，使用activate激活某个环境
source activate env_name

# 退出虚拟环境
source deactivate env_name

# 删除一个已有的环境
conda env remove -n env_name

# 查看已安装的环境
conda info -e

 ```
 
 ### Conda的包管理
 
 ####
 ```
# 安装scipy
conda install scipy

# 查看当前环境下已安装的包
conda list

# 查看某个指定环境的已安装包
conda list -n env_name

# 安装package
conda install -n python34 numpy

 ```

## CUDA
* [CUDA是什么鬼？](https://baike.baidu.com/item/CUDA/1186262?fr=aladdin)
  [PPA是什么鬼？](http://blog.csdn.net/baidu_22502417/article/details/46683549)
  [参考教程1](http://blog.csdn.net/autocyz/article/details/52299889/)
  [参考教程2](http://blog.csdn.net/u010837794/article/details/63251725)
  
* First Install nvidia driver：
go to the [official sit](http://www.nvidia.com/Download/index.aspx?lang=en-us) to query your graphics driver version number, eg: 390

then
```
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt-get update
sudo apt-get install nvidia-390(change to your version number)
sudo apt-get install mesa-common-dev
sudo apt-get install freeglut3-dev
```

then reboot 
```
sudo reboot
```

check
```
nvidia-smi 
```
* install cuda 
first download cuda from [cuda8 offical site](https://developer.nvidia.com/cuda-toolkit-archive), recommend the .sh file

<div style="align: center">
 
<img src=https://github.com/MinglangQiao/Tools_and_Scripts/raw/master/images/Environment/CUDA_Dowload.png width="600" >

</div>

then

```
# don't need to install the NDIA Accelerated Graphics Driver, others use the default
sudo sh cuda_8.0.27_linux.run

```
as the result

<img src=https://github.com/MinglangQiao/Tools_and_Scripts/raw/master/images/Environment/install_cuda_sh.png width="900" >

next
```
sudo gedit /etc/profile

# add the following in the last row, without blank row
export PATH=/usr/local/cuda-8.0/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda-8.0/lib64$LD_LIBRARY_PATH

# ldconfig
sudo ldconfig      #使链接生效 

```

test cuda saples
```
cd /usr/local/cuda-8.0/samples/1_Utilities/deviceQuery
sudo make
./deviceQuery
```
and see

<img src=https://github.com/MinglangQiao/Tools_and_Scripts/raw/master/images/Environment/install_cuda_succeed.png width="900" >

## install cuDNN
first， go to the [official site](https://developer.nvidia.com/cudnn)to download the cudnn, register required

<img src=https://github.com/MinglangQiao/Tools_and_Scripts/raw/master/images/Environment/download_cuDNN.png width="900" >

upzip the file, and cd进入cudnn解压之后的include目录
```
sudo cp cudnn.h /usr/local/cuda-8.0/include/    #复制头文件
```
cd进入解压后的lib64目录下的动态文件进行复制和链接：
```
sudo cp -a libcudnn* /usr/local/cuda-8.0/lib64/    #复制动态链接库，-a 在保留原文件属性的前提下复制文件

```

[更改cudnn版本](https://blog.csdn.net/l297969586/article/details/67632608)
