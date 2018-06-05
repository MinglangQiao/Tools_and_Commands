# github help官网

https://help.github.com/

https://help.github.com/categories/collaborating-with-issues-and-pull-requests/

[老廖的教程](https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)

## 同步一个fork

https://gaohaoyang.github.io/2015/04/12/Syncing-a-fork/


## 更新远程仓库到本地
直接pull不行时先fetch， 再merge， 在merge时解决冲突
```
# 拉取更新

git fetch origin branch1 

# 将远程的mater和本地仓库合并
 
git merge origin/master

```
git pull命令的作用是：取回远程主机某个分支的更新，再与本地的指定分支合并，它的完整格式稍稍有点复杂
```
git pull <远程主机名> <远程分支名>:<本地分支名>
```

比如，要取回origin主机的next分支，与本地的master分支合并，需要写成下面这样 -
```
git pull origin next:master
```

## remote 的添加与删除

### 在本地目录下关联远程repository ：
#### 每个仓库下都有一个默认的origin 不用再添加origin， 先用git remote -v 查看一下
```
git remote add origin git@github.com:git_username/repository_name.git
```
#### 取消本地目录下关联的远程库：
 ```
git remote remove origin

```
### 版本回退

HEAD指向的版本就是当前版本，因此，Git允许我们在版本的历史之间穿梭，使用命令：
```
git reset --hard commit_id。
```
穿梭前，用：～可以查看提交历史，以便确定要回退到哪个版本。
```
git log
```


要重返未来，用：～查看命令历史，以便确定要回到未来的哪个版本。reflog命令显示整个本地仓储的commit，包括所有branch的commit，甚至包括已经撤销的commit
```
git reflog
```
退出git log 状态按 ： Q

### 关于分支
[参考资料](https://www.cnblogs.com/utank/p/7880441.html)

* 删除一个非当前所处分支
```
git branch -d <branch_name>
```
* 强制删除一个正打开的分支
```
git branch -D <branch_name>
```
* 删除被恢复的分支(Git会自行负责分支的管理，所以当我们删除一个分支时，Git只是删除了指向相关提交的指针，但该提交对象依然会留在版本库中)

如果知道分支的commit id
```
git branch <branch_name> <hash_val>
```
如果不知道分支的commit id， 用reflog命令将它找出来， 再恢复
```
git branch <branch_name> HEAD@{x}
```

### 快进式推送(FastForwards)与非快进式推送(NonFastForwards)

简介：http://blog.csdn.net/u010506504/article/details/43965627

### fork别人的项目后怎样同步更新别人的提交

1、推荐[在github上同步](https://www.cnblogs.com/mff520mff/archive/2017/08/13/7355118.html)，可以方便的查看和修改冲突的地方
注意把base fork改为自己的fork， head fork 改为作者的repo. 如果出现There isn’t anything to compare.是因为把base fork和 head fork弄成一样的的，可以先选择一个其他人的fork帮助完成base fork和head fork的设置


如果还是无法合并，请根据命令行的提示操作，就可以解决。不过要查一下每个命令什么意思，不要随便git rm

如果还是不行，就把对应文件删了换成作者的文件，解决问题最重要，变通

2、[命令行同步](https://blog.csdn.net/qq1332479771/article/details/56087333)
```
git remote -v 
git remote add upstream git@github.com:xxx/xxx.git
git fetch upstream
git merge upstream/master
git push 

```

## 解决冲突

https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/001375840202368c74be33fbd884e71b570f2cc3c0d1dcf000


## 关键节点或者完成某项工作后就要及时commit， 方便以后查找和回滚


## 解决git push 每次都需要输用户名和密码的问题
[参考资料](https://blog.csdn.net/toyijiu/article/details/73611874)

git push -u origin master 如果当前分支与多个主机存在追踪关系，则可以使用 -u 参数指定一个默认主机，这样后面就可以不加任何参数使用git push，
不带任何参数的git push，默认只推送当前分支，这叫做simple方式

## 删除某次commit
https://www.36nu.com/post/275
