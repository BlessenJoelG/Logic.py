nums = [1,13,10,12,31]
s = str(nums)[1:-1]
s = s[::-1]
l = s.split(" ,")
l = list(map(int, l))
print(l)
nums += l