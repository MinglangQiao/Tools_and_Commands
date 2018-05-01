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

[关于shadowsocks的介绍](http://www.360doc.com/content/16/1009/23/1489589_597192113.shtml)

#### 双屏显示， 旋转一个屏幕， 不用每次开机都设置
ubuntu 》》 系统设置 》》 显示 》》 旋转 

xserver每次开机都要重新设置，还是该google直接搜想要的问题， 关键字都打上：
ubuntu multi screen xserver rotate
get：https://ubuntuforums.org/showthread.php?t=1835721


#### ubuntu 循环登录怎么办
* 不要随便听信网上的话把profile给删掉了， 删完连cp sudo命令都没有了，即使删也要有备份

* 如果没有了ls， cp等命令，首先应该google关键词的[ls, mv, cp, cat, vi, command not found](https://unix.stackexchange.com/questions/270585/ls-mv-cp-cat-vi-command-not-found)

这些命令一般在/bin下， 所以可以加上前缀 /bin/ls,  /bin/cp等等。

* 如果sudo也不行了， 也应该google关键词[Ubuntu 12.04 LTS bash: sudo: command not found [closed]
](https://stackoverflow.com/questions/15596278/ubuntu-12-04-lts-bash-sudo-command-not-found)

sudo命令在/usr/bin/下，使用/usr/bin/sudo即可， 然后cp /etc/profile_bak /etc/profile

或者先su -获取root权限， 然后cp /etc/profile_bak /etc/profile

重要把命令恢复了

如果sudoers出问题了
[参考这里](https://blog.csdn.net/mr_pang/article/details/51732900)
安装前先su -获得root权限

* 


#### 如果不能上网
先看看ip地址有没有
```
ifconfig
```

如果没有，执行一下命令，应该就有了，然后就能联网了
```
sudo dhclient
```

[设置静态ip](https://blog.csdn.net/xiaohuozi_2016/article/details/54743992), DNS服务器可以在
windows下执行下列命令，查看。 但是又会导致连不网
```
ipconfig /all
```
