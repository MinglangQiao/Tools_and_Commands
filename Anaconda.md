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

