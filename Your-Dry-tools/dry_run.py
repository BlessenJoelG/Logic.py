num,tot = [4,3,2,1],""
for x in (num):
    tot = tot + str(x)
tot = str(int(tot)+1)
num = [int(x) for x in tot]
print(num)