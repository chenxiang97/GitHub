"""
函数和代码复用
定义与使用
函数：是一段具有特定功能的、可重用的语句组
    是一种功能的抽象，表达特定功能
    降低编程维度，实现代码复用
def <函数名>(<参数(0个或多个)>) :
    <函数体>
    return <返回值>

def fact(n, *b) :
    s = 1                       
    for i in range(1,n+1) :
        s *= i
    for item in b :
        s *= item
    return s    #   传递返回值：一个或多个

#   函数的调用
a = fact(10, max(3, 5, 8))
print(a)

"""

ls = ["F", "f"]     #通过使用 [] 真实创建了一个全局变量列表ls
def func(a) :
    ls = []         #真实创建了，ls 变为局部变量
    ls.append(a)    #在 ls 列表中增加一个元素
    return
func("C")
print(ls)