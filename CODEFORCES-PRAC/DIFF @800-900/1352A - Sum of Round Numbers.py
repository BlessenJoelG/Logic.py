t = int(input())
for _ in range(t):
    num = int(input())
    num = str(num)
    lst=[]
    num_z = (len(num)-1)
    idx = 0
    while(num_z>=0):
        if num[idx]!="0":
            lst.append((num[idx]+"0"*num_z))
        idx = idx+1
        num_z = num_z-1
    print(len(lst))
    print(" ".join(lst))
