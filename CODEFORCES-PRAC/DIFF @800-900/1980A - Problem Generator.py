t = int(input())
for _ in range(t):
    m_n = list(map(int, input().split()))
    diff_lvl = {"A","B","C","D","E","F","G"}
    ques_1 = list(input())
    ques_2 = {x for x in ques_1}
    extra = 0
    for ch in ques_2:
        if ques_1.count(ch) < m_n[1]:
            extra += (m_n[1] - ques_1.count(ch))
    print((len(diff_lvl - ques_2) * m_n[1]) + extra)