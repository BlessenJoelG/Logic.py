for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split())) 
    freq = {}
    found = -1 
    for x in arr:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1   
        if freq[x] == 3:
            found = x
            break
    print(found)