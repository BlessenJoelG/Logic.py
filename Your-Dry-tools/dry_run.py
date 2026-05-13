n,mul = 31,0
digsplit = [int(x) for x in str(n)]
mul = max(digsplit)
digsplit.remove(max(digsplit))
mul = mul*max(digsplit)
print(mul)