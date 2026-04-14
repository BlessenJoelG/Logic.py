m,c = 0,0
for _ in range(int(input())):
    m_c = list(map(int,input().split()))
    if m_c[0]>m_c[1]:
        m += 1
    elif m_c[0]<m_c[1]:
        c += 1
if m > c:
    print("Mishka")
elif m < c:
    print("Chris")
elif m == c:
    print("Friendship is magic!^^")