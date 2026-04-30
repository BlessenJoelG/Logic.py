grid,c = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]],0
for lst in grid:
    for x in lst:
        if x<0:
            c += 1
print(c)