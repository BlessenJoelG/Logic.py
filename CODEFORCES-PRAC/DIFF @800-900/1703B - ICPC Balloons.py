t = int(input())
for x in range(t):
    n = int(input())
    solve_ord = input()
    str_chk,tot_loons = set(),0
    for _ in solve_ord:
        if _ not in str_chk:
            str_chk.add(_)
            tot_loons = tot_loons + 2
        elif _ in str_chk:
            tot_loons = tot_loons + 1
    print(tot_loons)
