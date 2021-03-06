## 安装
去[这里](http://www.jetbrains.com/pycharm/download/previous.html)下载安装包
```
cd /home/ml/pycharm-2017.3.4/bin
./pycharm.sh

```

1、在pycharm中，安装过的包 显示没有这个包的解决方案
先
```
whereis python ## 查看python位置
```
然后参考：[解决办法](https://blog.csdn.net/u012322855/article/details/78991559?%3E)

2、[pycharm主题](http://profeel.github.io/2016/05/18/Pycharm%E4%B8%BB%E9%A2%98%E8%AE%BE%E7%BD%AE/)

3、[关闭拼写检查](https://blog.csdn.net/langzi7758521/article/details/50997072)

4、[进入虚拟环境](https://blog.csdn.net/liangyihuai/article/details/77842628)

5、[不能导入cv2, 先找到cv2的路径](https://blog.csdn.net/heroacool/article/details/50967281)

6、[给pycharm添加快捷方式](http://www.jb51.net/article/130534.htm)

7、[设置ruler_line](https://www.cnblogs.com/dengyg200891/p/6061752.html)

8、[jupyter notebook](http://zhuangzhuang.github.io/2017/01/22/fix-pycharm-jupyter/)

9 [pycharm启动后总是在index很慢，不能运行程序](https://www.zhihu.com/question/47427720/answer/106059581)
```
将不想索引的文件夹设置为Excluded Folders即可
```

## Debug
[Debug按钮的用法](https://www.jianshu.com/p/64a45714c58c)

[官方文档](https://www.jetbrains.com/help/pycharm/jumping-to-cursor.html)

5个调试按钮：

Jumping to Cursor：If one would like to re-debug starting from a particular line, even if this line is located "up-stream", PyCharm provides such a possibility. Thus one will avoid the necessity to finalize debugging prior to re-debug

## 怎样申请专业版和远程连服务器调试代码
[申请教程](http://www.pythontip.com/blog/post/13119/)

[远程调试教程](https://www.cnblogs.com/xiongmao-cpp/p/7856596.html)

Root path 是远程服务器的工作路径

<img src=https://github.com/MinglangQiao/Tools_and_Scripts/raw/master/images/Tools/pycharm_server.png width="600" >


 Web path 的设置，应该是用来配置网页上查看文件的服务，可以无视
 
 选择解释器为远程的解释器， 通过Remote host查看远程主机上的文件

[官方教程](https://www.jetbrains.com/help/pycharm/creating-a-remote-server-configuration.html)

### 1. 通过Tools > Deployment > Configuration配置远程主机IP、Rootpath; 然后mapping设置本地文件夹（注意Deploy path on server 这里填写相对于root path的目录，注意两个路径连起来的文件夹要和本地文件夹对应上，绿色的部分表示是同步的。可以随时更改，注意点刷新图标）

<img src=https://github.com/MinglangQiao/Tools_and_Scripts/raw/master/images/Tools/pycharm_path.png width="900" >

如果你想看到更多的文件，就把root path 变短一点，比如， root path为/home/s/ml，  Deployment path为/DIEM时可以看到
<img src=https://github.com/MinglangQiao/Tools_and_Scripts/raw/master/images/Tools/pycharm_rootpath.png >

### 1.5 [Specifying user credentials defined during registration on the host](https://www.jetbrains.com/help/pycharm/creating-a-remote-server-configuration.html)

### 2、 通过settings > Projetc Interpreter > Project Interpreter > 小齿轮 > add remote(2018.1版本没有这个选项， BUG， 换成2017的就有了) > SSH Interpreter > 配置远程服务器的解释器

### 3、通过Tools > Deployment > Browst Remote Host 查看远程的文件， 点击文件并编辑， upload; 通过Tools > Deployment > Upload to 和download from 上传和下载文件


### 怎样设置自动上传
首先需要在Tools > Deployment > Mappings > 将对应的server设置为Use this server as default
https://my.oschina.net/cerise/blog/886282

### 生成和安装requirements.txt
https://blog.csdn.net/luocheng7430/article/details/80373572


## 太卡怎么办
1 https://confluence.jetbrains.com/pages/viewpage.action?pageId=25788581
2 http://www.mamicode.com/info-detail-2208329.html
