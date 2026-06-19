text = "leet code"
brokenLetters = "e"
text = text.split(" ")
ans = 0
brokenletters = [x for x in brokenLetters]
for word in text:
    for letter in brokenLetters:
        if word.count(letter)>0:
            ans = ans + 1
            break
print(len(text)-ans)