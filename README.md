# python GUI 教程

```
sudo apt-get install python3-dev python3-setuptools
```

### upgrade pip

```
pip3 install --upgrade pip
```

### if cannot import name main

```
sudo nano /usr/bin/pip3
```

content:

```
from pip import __main__
if __name__ == '__main__':
    sys.exit(__main__._main())
```

### install Pillow

```
sudo pip3 install Pillow
```

or

```
pip install -i https://pypi.douban.com/simple pillow
```

所有课件皆使用python3

### tkinter

* 第1课 简单的GUI
* 第2课 封装成class
* 第3课 增加点击事件
* 第4课 按照数据、布局、事件结构划分
* 第5课 指定按钮大小

### qt4
