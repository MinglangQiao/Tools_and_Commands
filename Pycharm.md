## 

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

### 1. 通过Tools > Deployment > Configuration配置远程主机IP、Rootpath; 然后mapping设置本地文件夹（注意Deploy path on server 这里填写相对于root path的目录， 直接写/即可）

<img src=https://github.com/MinglangQiao/Tools_and_Scripts/raw/master/images/Tools/pycharm_path.png width="600" >


### 2、 通过settings > Projetc Interpreter > Project Interpreter > 小齿轮 > add > SSH Interpreter > 配置远程服务器的解释器

### 3、通过Tools > Deployment > Browst Remote Host 查看远程的文件， 点击文件并编辑， upload; 通过Tools > Deployment > Upload to 和download from 上传和下载文件


 
 
