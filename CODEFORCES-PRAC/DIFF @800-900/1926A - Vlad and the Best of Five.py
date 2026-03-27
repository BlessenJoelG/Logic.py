t = int(input())
for _ in range(t):
    lttr = [_ for _ in (input())]
    if lttr.count("A")>lttr.count("B"):
        print("A")
    else:
        print("B")
