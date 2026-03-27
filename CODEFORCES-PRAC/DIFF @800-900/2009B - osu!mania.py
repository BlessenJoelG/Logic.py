t = int(input())
bot_top = []
for _ in range(t):
    n = int(input())
    for _ in range(n):
        note_lines = [_ for _ in (input())]
        bot_top.append(note_lines.index("#")+1)
    bot_top.reverse()
    print(*bot_top)
    bot_top.clear()
