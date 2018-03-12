# github help官网

https://help.github.com/

https://help.github.com/categories/collaborating-with-issues-and-pull-requests/


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


要重返未来，用：～查看命令历史，以便确定要回到未来的哪个版本。
```
git reflog
```
退出git log 状态按 ： Q



## 快进式推送(FastForwards)与非快进式推送(NonFastForwards)

简介：http://blog.csdn.net/u010506504/article/details/43965627


## 解决冲突

https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/001375840202368c74be33fbd884e71b570f2cc3c0d1dcf000
