t = int(input())
div_chck,ste = [],[]
for _ in range(t):
    div_chck.extend(map(int,input().split()))
    if(div_chck[0]%div_chck[1]==0):
        ans = 0
        ste.append(ans)
    else:
        r = div_chck[0]%div_chck[1]
        ans = div_chck[1] - r
        ste.append(ans)
    div_chck.clear()
for _ in range(len(ste)):
    print(ste[_])
