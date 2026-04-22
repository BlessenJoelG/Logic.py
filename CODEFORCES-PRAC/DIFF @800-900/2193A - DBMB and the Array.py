for _ in range(int(input())):
    n_s_x = list(map(int,input().split()))
    nums = list(map(int,input().split()))
    if sum(nums) <= n_s_x[1] and (n_s_x[1]-sum(nums))%n_s_x[2]==0:
        print("YES")
    else:
        print("NO")