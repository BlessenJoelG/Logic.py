costs = [1,3,2,4,1]
coins = 7
costs.sort()
c = 0
for price in costs:
    if price<=coins:
        coins -= price
        c += 1
    else:
        break
print(c)