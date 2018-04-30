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

 [参考中文安装教程](https://blog.csdn.net/yhaolpz/article/details/71375762)
 
 注意： 1）第9步和第10部那里make时不要sudo权限
 
       2） make前把python环境改为系统的默认环境
       暂时办法
   
        sudo rm /usr/bin/python
        sudo ln -s /usr/bin/python2.7 /usr/bin/python
        PATH=/usr/bin:$PATH
        
        永久修改
        
 
 * ImportError: dynamic module does not define module export function (PyInit__caffe)
 
[python 版本不能太高](https://stackoverflow.com/questions/34295136/importerror-dynamic-module-does-not-define-module-export-function-pyinit-caff)

 
* m//home/yali/anaconda2/lib/libpng16.so.16：对‘inflateValidate@ZLIB_1.2.9’未定义的引用

[解决办法1](https://blog.csdn.net/ruotianxia/article/details/78437464)

[如果办法1不行](https://stackoverflow.com/questions/48306849/lib-x86-64-linux-gnu-libz-so-1-version-zlib-1-2-9-not-found)

* /sbin/ldconfig.real: /usr/local/cuda-8.0/lib64/libcudnn.so.5 

[解决办法](https://blog.csdn.net/m0_37407756/article/details/70789271)， 如果不行关掉终端重新打开编译

* 关于训练caffe模型出现./build/tools/caffe: command not found

[解决办法](https://blog.csdn.net/xunan003/article/details/72997028)



## 方法3： 虚拟环境下安装caffe， 参考这个教程装(有bug没解决)

https://yangcha.github.io/Caffe-Conda3/


