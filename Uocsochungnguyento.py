import math
def nguyento(n) :
    if n < 2 : return False
    for i in range(2, int(math.sqrt(n)) + 1) :
        if n % i == 0 : return False
    return True
t = int(input())
for i in range(t) :
    a, b = [int(i) for i in input().split()]
    c = math.gcd(a, b)
    s = 0
    while c > 0 :
        s += c % 10
        c = int(c / 10)
    if nguyento(s) == True : print("YES")
    else : print("NO")