### 1： python SyntaxError: non-default argument follows default argument
[默认参数不能放在非默认参数的前边](http://blog.csdn.net/VonSdite/article/details/76796360)


#### 学习一下多线程
[原理讲解](https://blog.csdn.net/luoweifu/article/details/46595285)
[廖雪峰教程](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319272686365ec7ceaeca33428c914edf8f70cca383000)

### 列表生成式而非for + append可以减少循环层数

eg ：
``` pyhton
all_data = [line.split() for line in lines]
```

比
``` python
for line in lines:
    line = line.split()
    all_data.append(line)
```

要简洁
