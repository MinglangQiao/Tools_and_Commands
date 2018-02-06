# github help官网

https://help.github.com/

https://help.github.com/categories/collaborating-with-issues-and-pull-requests/


## 同步一个fork

https://gaohaoyang.github.io/2015/04/12/Syncing-a-fork/


## 更新远程仓库到本地
```
# 拉取更新

git fetch origin branch1 

# 将远程的mater和本地仓库合并
 
git merge origin/master

```

## remote 的添加与删除

# 在本地目录下关联远程repository ：
#### 每个仓库下都有一个默认的origin 不用再添加origin， 先用git remote -v 查看一下
```
git remote add origin git@github.com:git_username/repository_name.git
```
#### 取消本地目录下关联的远程库：
 ```
git remote remove origin

```


