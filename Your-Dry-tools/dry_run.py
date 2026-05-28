def chk(n,a):
    if n.startswith(x) == False and n.count(x)>=1:
        return True
    else:
        return False
n = 101
x = 0
n = str(n)
x = str(x)
print(chk(n,x))