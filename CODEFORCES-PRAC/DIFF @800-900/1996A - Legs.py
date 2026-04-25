for _ in range(int(input())):
    n = int(input())
    cows = n // 4         
    rem = n % 4          
    if rem == 0:
        print(cows)
    else:
        print(cows + 1)    