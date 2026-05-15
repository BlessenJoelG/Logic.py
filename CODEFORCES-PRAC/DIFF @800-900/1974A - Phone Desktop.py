import math
for _ in range(int(input())):
    x, y = map(int, input().split())
    screens = math.ceil(y / 2)
    free = screens * 15 - y * 4
    if x > free:
        screens += math.ceil((x - free) / 15)
    print(screens)
