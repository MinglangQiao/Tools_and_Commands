1、安装依赖
```
# 安装编译工具
sudo apt-get install build-essential

# 安装依赖包
sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev

# 安装可选包
sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev
```

2、到[官网](https://opencv.org/releases.html)下载opencv-3.3.0 

3、 解压， 编译安装
```
cd opencv-3.3.0 

mkdir release

cd release

# 注意 .. 不能省略
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local ..

# j4表示开8个线程来进行编译
make -j8 

sudo make install
```

4、相关配置
```
# 将opencv的库加入到路径，从而让系统可以找到
sudo gedit /etc/ld.so.conf.d/opencv.conf
 
末尾加入下面两行
include /etc/ld.so.conf.d/*.conf
/usr/local/lib
，保存退出

# 使配置生效
sudo ldconfig    

sudo gedit /etc/bash.bashrc 

末尾加入下面两行
PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/lib/pkgconfig
export PKG_CONFIG_PATH

# 使配置生效
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
