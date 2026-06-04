for _ in range(int(input())):
     n = int(input())
     nums = list(map(int,input().split()))
     eve_chk,odd_chk = False,False
     if sum(nums)&1 == 1:
        print("YES")
     else:
        for x in nums:
            if x&1 == 1:
                odd_chk = True
                break
        for x in nums:
            if x&1 != 1:
                eve_chk = True
                break
        if odd_chk == eve_chk:
            print("YES")
        else:
            print("NO")