for _ in range(int(input())):
    n = int(input())
    y = n % 2020
    x = (n - 2021 * y) // 2020
    if x >= 0:
        print("YES")
    else:
        print("NO")
      
