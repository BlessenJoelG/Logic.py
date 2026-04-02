edges,lst = [[1,2],[5,1],[1,3],[1,4]],[]
for x in edges:
    lst.extend(x)
for _ in lst:
    if lst.count(_) == len(edges):
        print(_)
        break