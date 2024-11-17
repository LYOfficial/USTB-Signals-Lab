# USTB-Signals-Lab
> USTB 自动化学院《信号与系统分析实验》指导与理论图像Python模拟

### 前言

本人作为一个《信号与系统》原课程没怎么学好就直接去做实验的人，做起实验来非常头疼，做完之后有了些经验，于是做了这个仓库，希望能帮助后面的同学。

### 实验指导

原指导书是 Word 格式，在做实验的时候使用平板电脑查看很容易漏掉操作步骤，于是重新使用 **Markdown** 优化了原指导书排版，并在每个实验末尾添加了一些心得和建议。

点击阅读：[信号与系统分析实验指导](https://github.com/LYOfficial/USTB-Signals-Lab/blob/main/GuideBook/0.md)

### 理论图像

后面实验理论分析图像有时难以画出，可以使用 Python 进行模拟，基本都是实验五和实验六的模拟图像。

点击查看：[Python 生成模拟信号图像](https://github.com/LYOfficial/USTB-Signals-Lab/tree/main/src)

### 操作方法

**1.安装 Python **

这个应该不用教吧，建议版本 3.11 。

**2.安装模块**

打开命令行，安装以下模块：

```
pip install numpy

pip install matplotlib
```

网络不好的话就在后面加上镜像源链接，例如：

```
pip install matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple
```

**3.启动程序**

打开命令行，执行程序：

```
python xxx.py
```

