import math
def nguyento(n) :
    if n < 2 : return False
    for i in range(2, int(math.sqrt(n)) + 1) :
        if n % i == 0 : return False
    return True
def check(n) :
    if nguyento(len(n)) == False : return False
    s1 = 0
    s2 = 0
    for i in n : 
        if nguyento(int(i)) == True : s1 += 1
        else : s2 += 1
    if s1 > s2 : return True
    return False
t = int(input())
for i in range(t) :
    n = input()
    if check(n) == True : print("YES")
    else : print("NO")