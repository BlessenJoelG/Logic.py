words = ["cd","ac","dc","ca","zz"]
seen = set()
count = 0
for word in words:
    rev = word[::-1]
    if rev in seen:
        count += 1
    else:
        seen.add(word)
print(count)