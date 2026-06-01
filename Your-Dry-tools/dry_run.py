c = 0
cost.sort(reverse=True)
print(cost)
for i in range(len(cost)):
    if i%3 != 2:
        c += cost[i]
print(c)