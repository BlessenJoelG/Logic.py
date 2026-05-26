n,x,y = map(int,input().split())
num = int(input())
a,b = str(num%10**x),str(10**y%10**x)
a = (abs(len(a)-len(b)))*"0"+a
b = (abs(len(a)-len(b)))*"0"+b
total = (1 for i in range(len(a)) if a[i]!=b[i])
print(sum(total))