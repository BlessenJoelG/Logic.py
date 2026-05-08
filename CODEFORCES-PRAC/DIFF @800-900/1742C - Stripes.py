for _ in range(int(input())):
    flag = False
    rows = []
    while len(rows) < 8:
        line = input().strip()
        if line:
            rows.append(line)
    for row in rows:
        if row == "RRRRRRRR":
            flag = True
    if flag == True:
        print("R")
    else:
        print("B")
