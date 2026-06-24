items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
ruleKey = "type"
ruleValue = "phone"
c = 0
if ruleKey == "type":
    x = 0
elif ruleKey == "color":
    x = 1
elif ruleKey == "name":
    x = 2
for item in items:
    if item[x] == ruleValue:
        c += 1
print(c)