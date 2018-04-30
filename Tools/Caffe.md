[官网安装教程](http://caffe.berkeleyvision.org/install_apt.html)

先安装虚拟环境
```
 conda create -n caffe python=3.5
 
 conda activate caffe
 
 conda deactivate
 
 [参考中文安装教程](https://blog.csdn.net/yhaolpz/article/details/71375762)
 
```

需要保证添加了cuda路径和安装了cudnn
```
sudo gedit ~/.bashrc
export LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH 

``

查看cuda版本对不对， 系统更新时可能会把cuda给更新了。以后不要随便更新系统文件了


```
cuda 版本 
cat /usr/local/cuda/version.txt

cudnn 版本 
cat /usr/local/cuda/include/cudnn.h | grep CUDNN_MAJOR -A 2
```
