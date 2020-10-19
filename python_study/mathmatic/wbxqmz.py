from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from sympy import * #用于求导积分等科学计算
from sympy.plotting import plot3d
from sympy.functions import exp
from sympy.series import series
from cmath import sin
from sympy.series import series
from matplotlib.pyplot import plot
from sympy.core import Symbol
 
x = Symbol('x')#x 变量
# print(help(plot))#对x = 0点泰勒展开 至x20次方无穷小 
 
p0 = plot(sin(x),(x,-2*pi,2*pi),line_color='b',ylim=(-1.5,1.5),title='funion',show=False)
#画出sin(x),范围-2*pi,2*pi，蓝色线，y刻度范围-1.5,1.5，暂不显示

exper1 = series(sin(x),x,n=4)#泰勒展开至第O(x**4)
p1 = plot(exper1.subs(O(x**4),0),(x,-2*pi,2*pi),line_color='br',title='O(x**4)',show=False)
#第O(x**4)项用0替代 颜色为蓝红色

exper2 = series(sin(x),x,n=6)#泰勒展开至第O(x**6)
p2 = plot(exper2.subs(O(x**6),0),(x,-2*pi,2*pi),line_color='g',title='O(x**6)',show=False)
#第O(x**6)项用0替代 颜色为绿

exper3 = series(sin(x),x,n=8)#泰勒展开至第O(x**8)
p3 = plot(exper3.subs(O(x**8),0),(x,-2*pi,2*pi),line_color='r',title='O(x**8)',show=False)
#第O(x**8)项用0替代 颜色为红

exper4 = series(sin(x),x,n=10)#泰勒展开至第O(x**10)
p4 = plot(exper4.subs(O(x**10),0),(x,-2*pi,2*pi),line_color='y',title='O(x**10)',show=False)
#第O(x**10)项用0替代 颜色为黄
p0.extend(p1)
p0.extend(p2)
p0.extend(p3)
p0.extend(p4)
p0.show()#显示图像
