import numpy as np
import sympy as sp
import matplotlib.pyplot as plt  # 绘制
from matplotlib.pyplot import MultipleLocator  # 导入此类，设置坐标轴间隔


def derivate(fuc, n):
    '''求解n阶导数'''
    derivation = fuc
    for i in range(n):
        derivation = sp.diff(derivation, x)
    return derivation


def fx_expanded_form_N(fx, n):
    '''求解n阶Taloy展开式 其中x0=0'''
    item_first = 0
    x = sp.Symbol('x')
    for i in range(1, n + 1):
        fx_expanded_form = derivate(fx, i).evalf(subs={x: 0}) * (x ** i) / np.math.factorial(i)
        item_first = item_first + fx_expanded_form
    return item_first

x = sp.Symbol('x')
fx = sp.sin(x)

for j in range(1, 51):
    plt.clf()  # 在画板上清除图像
    y = fx_expanded_form_N(fx, j)  # 第j阶的Taloy展开式
    print(j, y)
    xn = np.arange(-20, 20, 0.1)
    yn = []
    for i in xn:
        yn.append(y.evalf(subs={x: i}))  # 得到j阶的Taloy展开式中y的列表
    plt.ion()  # 开启交互模式,这样每个绘图命令之后添加自动图形更新
    '''设置x的刻度值'''
    x_major_locator = MultipleLocator(1)
    ax = plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)

    plt.xlabel("x")
    plt.ylabel("sin(x)")

    plt.ylim(-2, 2)  # y轴的范围
    plt.grid()  # 在背景中加上方格
    plt.plot(xn, yn)
    plt.pause(0.1)  # 当前图像悬停一会
plt.ioff()  # 要关闭交互模式,否则图像会一闪而过
plt.show()