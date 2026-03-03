n_k = list(map(int,input().split()))
def fact_prod(x):
    if x == 0:
        return 0
    prod_sum = x*5 + fact_prod(x-1)
    return prod_sum
for _ in range(n_k[0],0,-1):
    if fact_prod(_)+n_k[1] <= 240:
        print(_)
        break
    elif fact_prod(_)+n_k[1] >240:
        print(0)
if n_k[1] == 240:
    print(0)