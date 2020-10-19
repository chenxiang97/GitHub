#random库:使用生成随机数的python标准库
"""
基本随机数函数：
seed(N):初始化给定的随机数种子，默认为当前系统时间
random():生成一个[0.0,1.0]之间的随机小数

扩展随机数函数：
randint(a,b):生成一个[a,b]之间的整数
gettrandbits(k)：生成一个 k 比特长的随机整数
uniform(a,b)：生成一个[a,b]之间的随机小数
randrange(m,n[,k])：生成一个[m,n)之间以 k 为步长的随机整数
choice(seq)：从序列中随机选择一个元素
shuffle(seq)：将序列seq中的元素随机排列，返回打乱后的序列
"""
#CalPiV1.py
#普通方法求解 Π 

pi = 0
N = 100
for k in range(N) :
    pi += 1/pow(16,k)*( \
        4/(8*k+1) - 2/(8*k+4) - \
        1/(8*k+5) - 1/(8*k+6))
print("圆周率值是: {}".format(pi))