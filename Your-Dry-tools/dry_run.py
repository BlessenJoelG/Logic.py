allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
allowed,ans = {x for x in allowed},0
for word in words:
    w = {x for x in word}
    if len(w.intersection(allowed)) == len(w):
        ans = ans + 1 
print(ans)