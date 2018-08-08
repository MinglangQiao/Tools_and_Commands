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

#### [装系统时花屏](https://blog.csdn.net/heroxuetao/article/details/41482511)

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

如果没有，执行一下命令，应该就有了，然后就能联网了;如果网关/ip这些设置都对但还是不能上网，也执行一下下面的语句
```
# dhclient命令可以释放你的电脑的IP地址并从DHCP服务器上获得一个新的
sudo dhclient
```

[设置静态ip](http://www.linuxdiyf.com/linux/23952.html), DNS服务器可以在系统设置》》 网络 》》 有线那查看
首先科普一下[网络配置的四大基本要素： IP + Netmask + Gateway + DNS](https://blog.csdn.net/fool_fool/article/details/8979694)

windows下这样查看IP地址和网关地址
```
ipconfig /all
```
ubuntu查看网关和DNS
```
# 网关
route -n

#DNS
通过设置》 网络 》 有线 查看DNS和默认路由
# cat /etc/resolv.conf
```
如果之前乱改过DNS，修改DNS为默认状态
```
sudo gedit /etc/network/interfaces
```
改成怎样即可， 只保留默认的，不要乱加其他的
```
nameserver 12x.x.1.1
```


然后
```
sudo gedit /etc/network/interfaces
```
gateway是网关地址，也就是路由器的ip地址，也就是通过windows下的 ipconfig /all或者uubuntu下没乱改前可以通过
route -n查看到的网关地址， 即192.168.xxx.x
```
内核 IP 路由表
目标            网关            子网掩码        标志  跃点   引用  使用 接口
0.0.0.0         192.168.xxx.x   0.0.0.0         UG    0      0        0 enp0s31f6
169.254.0.0     0.0.0.0         255.255.0.0     U     1000   0        0 enp0s31f6
192.168.226.0   0.0.0.0         255.255.255.0   U     0      0        0 enp0s31f6

```

改成这样
```
auto lo
iface lo inet loopback
auto enp0s31f6
iface enp0s31f6 inet static
address 192.168.226.xxx
netmask 255.255.255.0
gateway 192.168.xxx.x
dns-nameserver 202.112.128.51
dns-nameserver 202.112.128.50
```
然后
```
sudo /etc/init.d/networking restart
```
不出意外会发现连不了有线：

1）显示灰色的设备未托管
```
sudo gedit /etc/NetworkManager/NetworkManager.conf
```
修改 managed=true
```
[main]
plugins=ifupdown,keyfile,ofono
dns=dnsmasq

[ifupdown]
managed=true
```
然后重启， 选择有线连接1（特别是登录校园网很慢时）， 再登录校园网就可以了

2) 选择桌面左上角网络图标那里的WIFI可以上网， wifi上网不需要登录哦。如果有线网速卡时可以用WIFI，貌似挺快的

总结：真的是要搞清楚原理和概念再做， 知道为什么，不要想当然，多查查资料，之前就是把网关地址瞎设成广播地址了，导致校园往登录巨慢，或者循环登录， 无法上网

## 新建账户并添加用户权限
https://www.linuxidc.com/Linux/2016-06/132218.htm


## 关于bash和profile
https://www.cnblogs.com/liaohuiqiang/p/7197581.html?utm_source=itdadao&utm_medium=referral

### 可以进入GRUB菜单，但是无法进入登录界面

  1 进入recover mode, 查看报错信息，google之
  
  2 找到一个答案： https://askubuntu.com/questions/885062/root-file-system-requires-manual-fsck/885085
  
  3 修复文件系统： sudo fsck -f /dev/sda1， repeat the fsck command if there were errors， 第二次就成功了
  
  4 type reboot
