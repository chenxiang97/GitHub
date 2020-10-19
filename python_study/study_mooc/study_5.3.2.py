"""
#将字符串 s 反转后输出
s[::-1]
def rvs(s) :
    if s == "" :
        return s
    else:
        return rvs(s[1:]) + s[0]
"""
"""
#斐波那契数列
def f(n) :
    if n == 1 or n == 2 :
        return 1
    else:
        return f(n-1) + f(n-2)
"""

#汉诺塔问题
count = 0
def hanoi(n, src, dst, mid) :
    global count
    if n == 1 :
        print("{}:{}->{}".format(1, src, dst))
        count += 1
    else:
        hanoi(n-1, src, mid, dst)
        print("{}:{}->{}".format(n, src, dst))
        count += 1
        hanoi(n-1, mid, dst, src)
print(hanoi(2, "A", "B", "C"))
print(count)