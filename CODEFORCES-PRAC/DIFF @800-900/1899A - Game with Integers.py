for _ in range(int(input())):
    n = int(input())
    if (n+1)%3 == 0 or (n-1)%3==0:
        print("First")
    else:
        print("Second")