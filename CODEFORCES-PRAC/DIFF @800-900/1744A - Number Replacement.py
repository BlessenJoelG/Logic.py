for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    word = input()
    mp = {}
    ok = True
    for i in range(n):
        if nums[i] in mp:
            if mp[nums[i]] != word[i]:
                ok = False
                break
        else:
            mp[nums[i]] = word[i]
    print("YES" if ok else "NO")