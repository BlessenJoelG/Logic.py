t = int(input())
for _ in range(t):
    n = int(input())
    notes = list(map(int,input().split()))
    res = ""
    for i in range(len(notes)-1):
        if (abs(notes[i]-notes[i+1]) == 5 or abs(notes[i]-notes[i+1]) == 7):
            res = "YES"
        else:
            res = "NO"
            break
    print(res)