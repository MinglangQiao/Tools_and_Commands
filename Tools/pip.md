用pip安装程序是加上  -i https://pypi.tuna.tsinghua.edu.cn/simple , 速度会很快
举个栗子：
## [久添加清华大学镜像](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/)
速度快到飞起


```
pip install opencv-python  -i https://pypi.tuna.tsinghua.edu.cn/simple
```

2、生成和安装requirements.txt
```
# 生成requirements.txt文件
pip freeze > requirements.txt

# 安装requirements.txt依赖
pip install -r requirements.txt

```
