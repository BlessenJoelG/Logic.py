h1,m1 = map(int,input().split(":"))
h2,m2 = map(int,input().split(":"))
t1,t2 = h1*60+m1,h2*60+m2
t = (t1+t2)//2
h,m = format(t//60,"02d"),format(t%60,"02d")
print(f"{h}:{m}")