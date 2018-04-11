###
#### Ubuntu每次开机后提示：检测到系统程序出现问题

解决方法
http://blog.csdn.net/smhbqc/article/details/43559947

原因解释：
https://linux.cn/article-5904-1.html


#### ubuntu 主题

http://www.ubuntuthemes.org/


#### ubuntu分区

[主分区和逻辑分区](http://www.cnblogs.com/and_he/archive/2011/10/18/2216492.html)
总共1.8T

第一步：10G 的主分区，用来挂载/boot

第二步：32G 的逻辑分区，用来挂载/swap，大小一般和内存一样大

第三步：100G  的逻辑分区，用来挂载/， 相当于windows的C盘

第四步：1.7T 的逻辑分区，用来挂载/home，相当于windows上面的Document，根据自己情况


#### *更改软件源为清华镜像
https://mirrors.tuna.tsinghua.edu.cn/help/ubuntu/

```
cd /etc/apt

#备个份
sudo cp sources.list sources.list.bak

# 修改
sudo gedit sources.list
```

#### * 安装chrome
去[官网](https://www.google.cn/chrome/)下载安装包
```
sudo dpkg -i google-chrome*
sudo apt-get -f install 
```

#### ubuntu下不能访问某些硬盘
https://www.cnblogs.com/565261641-fzh/p/5695819.html

#### 如何修复ubuntu中检测到系统程序错误的问题
https://blog.csdn.net/hywerr/article/details/72582082


#### ubuntu下安装shadowshocks QT5 和 配置 SwitchOmega
https://www.cnblogs.com/superxuezhazha/p/6065992.html

[关于shadowsocks的介绍](http://www.360doc.com/content/16/1009/23/1489589_597192113.shtml）
