### 安装Opencv，编译源码方式
[参考资料](https://blog.csdn.net/lgh0824/article/details/78487234)

1、安装依赖
```
# 安装编译工具
sudo apt-get install build-essential

# 安装依赖包
sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev

# 安装可选包
sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev
```

2、到[官网](https://opencv.org/releases.html)下载opencv

3、 编译安装
```
cd opencv-2.4.13

mkdir release

cd release

# 注意 .. 不能省略
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local ..

# j4表示开4个线程来进行编译
make -j4   

sudo make install
```

4、相关配置
```
# 将opencv的库加入到路径，从而让系统可以找到
sudo gedit /etc/ld.so.conf.d/opencv.conf

末尾加入 /usr/local/lib，保存退出

# 使配置生效
sudo ldconfig    

sudo gedit /etc/bash.bashrc 

末尾加入 PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/lib/pkgconfig

export PKG_CONFIG_PATH

# 使配置生效
sudo source /etc/bash.bashrc  

source /etc/bash.bashrc

 # 更新database
sudo updatedb

```

5、测试
```
python

>>> import cv2
>>> cv2.__version__
'2.4.13'
```

### 卸载opencv
```
cd 进入release文件夹

sudo make uninstall

cd ..

sudo rm -r release

sudo rm -r /usr/local/include/opencv2 /usr/local/include/opencv /usr/include/opencv /usr/include/opencv2 /usr/local/share/opencv /usr/local/share/OpenCV /usr/share/opencv /usr/share/OpenCV /usr/local/bin/opencv* /usr/local/lib/libopencv

```
