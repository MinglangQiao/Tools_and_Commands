[菜鸟链接](http://www.runoob.com/w3cnote/google-python-styleguide.html)

[Google文档](http://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/)

[读取视频的某一帧](https://blog.csdn.net/aa846555831/article/details/52382173)
使用imageio， 读到的image直接是array（RGB值）， 可以用matplotlib显示

```
import imageio
import matplotlib.pyplot as plt

reader = imageio.get_reader('A380.mp4')
for i, im in enumerate(reader):
    image = im
    plt.imshow(im)
    plt.show()
    print('Mean of frame %i is %1.1f' % (i, im.mean()))
    
```

2、读取txt的标准办法，多用列表生成式，可以使代码更简洁
```python
f = open(data_path, 'r')
lines = f.readlines()
all_data = [line.split() for line in lines]
```

3、[__init__.py的作用](https://www.cnblogs.com/AlwinXu/p/5598543.html)



4 sorted 函数，排序
http://www.runoob.com/python/python-func-sorted.html
