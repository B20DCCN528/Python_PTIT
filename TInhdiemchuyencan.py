t = int(input())
m = {}
for i in range(t):
    maSV = input()
    ten = input()
    lop = input()
    m[maSV] = [ten, lop]
for i in range(t):
    maSV, cc = input().split()
    d = 10
    for j in cc:
        if j == 'm' : d -=1
        elif j == 'v' : d -= 2
    if d < 0 : d = 0
    m[maSV] = m[maSV] + [d] 
for i in m:
    print(i, end = ' ')
    for j in m[i] :
        print(j, end = ' ')
    if(m[i][-1] == 0) : print('KDDK')
    else : print()