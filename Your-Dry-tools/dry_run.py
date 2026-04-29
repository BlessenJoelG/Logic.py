n = "886996"
# for i in range(len(n)):
#     if i & 1 == 0:
#         res.append(int(n[i]))
#     else:
#         res.append(-1*int(n[i]))
# print(res)
# print(sum(res))
num = sum(int(n[i]) if i & 1 == 0 else -1*int(n[i]) for i in range(len(n)))
print(num)