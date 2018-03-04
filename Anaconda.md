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

