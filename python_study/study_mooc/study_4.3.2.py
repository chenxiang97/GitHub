#CalPiV2.py
#蒙特卡罗方法求解 Π 
from random import random
from time import perf_counter   #为程序运行进行计时的一个函数

DARTS = 1000*1000
hits = 0.0
start = perf_counter()

for i in range(1,DARTS+1) :
    x,y = random(), random()
    dist = pow(x**2 + y**2, 0.5)
    if dist <= 1.0 :
        hits = hits + 1
pi = 4*(hits/DARTS)

print("圆周率值是: {}".format(pi))
print("运行的时间是：{:.5f}s".format(perf_counter() - start))