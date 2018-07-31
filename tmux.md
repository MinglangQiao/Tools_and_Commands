## inite

### 1 [参考教程1](http://louiszhai.github.io/2017/09/30/tmux/)

#### Tmux的优点：
   
   1) 丝滑分屏(split): tmux窗口中，新开的pane，默认进入到之前的路径，如果是ssh连接，登录状态也依旧保持着
   
   2) 保护现场（attach):  即使命令行的工作只进行到一半，关闭终端后还可以重新进入到操作现场，继续工作
  
#### 安装：
```
sudo apt-get install tmux
```

 #### 基本概念：
 
 ##### 1) session - window - panel
 一个tmux session（会话）可以包含多个window（窗口）， 一个window又可以包含多个pane（面板）， 这些面板适合运行相关性高的任务，以便同时观察到它们的运行情况
 
 figure: 示意图
 
  ##### 2) session
 
   创建一个session： 
   ```
   tmux new -s demo
   ```
   
   断开一个session：
   ```
   Ctrl + b + d
   或者
   tmux detach 
   ```
 
   进入之前的session
   ```
   tmux a -t session-name
   或者
   tmux a # 进入第一个session
   ```
   
   kill一个session：
   ```
   # 关闭一个session
   tmux kill-session -t session-name
   # 关闭所有session
   tmux kill-server
   ```
   
   查看所有session
   ```
   tmux ls
   ```
   如果刚好处于会话中， 可用对应的tmux快捷键Ctrl+b + s，此时tmux将打开一个会话列表，按上下键(⬆︎⬇︎)或者鼠标滚轮，可选中目标会话，按左右键（⬅︎➜）可收起或展开会话的窗口，选中目标会话或窗口后，按回车键即可完成切换
   
#### Tmux 快捷键：

##### 系统指令
| 前缀  | 指令 | 描述 | 
| :---:  | :---:  | :---:  |
| ctrl + b  | d | 断开当前会话 |


##### window指令
| 前缀  | 指令 | 描述 | 
| :---:  | :---:  | :---:  |
| ctrl + b  | c | 新建窗口 |
| ctrl + b  | & | 关闭窗口 |
| ctrl + b  | 0-9 | 切换到指定窗口 |
| ctrl + b  | p | 切换到上一窗口 |
| ctrl + b  | n | 切换到下一窗口 |
| ctrl + b  | w | 打开窗口列表， 用于切换窗口 |


##### pannel指令
| 前缀  | 指令 | 描述 | 
| :---:  | :---:  | :---:  |
| ctrl + b  | " | 当前面板上下一分为二，下侧新建面板 |
| ctrl + b  | % | 当前面板左右一分为二，右侧新建面板 |
| ctrl + b  | x | 关闭当前面板（关闭前需输入y or n确认） |
| ctrl + b  | q | 显示面板编号，在编号消失前输入对应的数字可切换到相应的面板 |
| ctrl + b  | { | 向前置换当前面板 |
| ctrl + b  | } | 向后置换当前面板 |
| ctrl + b  | 方向键 | 选择下一面板 |
| ctrl + b  | o | 向前置换当前面板 |
| ctrl + b  | Alt + 方向键 | 以5个单元格为单位调整当前面板边缘 |
| ctrl + b  | Ctrl + 方向键 | 以1个单元格为单位调整当前面板边缘 |

#### 灵活的配置

##### 修改指令前缀

   Ctrl+b指令前缀更换为距离更近的Ctrl+a组合键

   打开配置文件
   ```
   ~/.tmux.conf
   ```
   输入
   ```
   set -g prefix C-a #
    unbind C-b # C-b即Ctrl+b键，unbind意味着解除绑定
    bind C-a send-prefix # 绑定Ctrl+a为新的指令前缀

    # 从tmux v1.6版起，支持设置第二个指令前缀
    set-option -g prefix2 ` # 设置一个不常用的`键作为指令前缀，按键更快些
   
   ```
   使生效，有如下两种方式
   ```
   1 restart tmux。
   2 在tmux窗口中，先按下Ctrl+b指令前缀，然后按下系统指令:，进入到命令模式后输入source-file ~/.tmux.conf，回车后生效。
   ```
   
   


   
   
   
   
