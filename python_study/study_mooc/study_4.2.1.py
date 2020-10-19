s = "PYTHON"
while s != "":
    for c in s :
        if c == "T" :
            break
        print(c, end="")

    #去除最后一个字符串
    s = s[:-1]  

"""
for c in "PYTHON":
    if c == "T":
        break
    print(c, end="")
"""