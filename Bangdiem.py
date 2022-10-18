from decimal import ROUND_HALF_UP, Decimal


id = 1
class HocSinh :
    maHS = 'HS'
    diemTB = 0
    xeploai = ''
    def __init__(self, ten, diem) :
        global id
        self.maHS += '{:02d}'.format(id)
        id += 1
        self.ten = ten
        x = 2 * diem[0] + 2 * diem[1]
        for i in range(2, 10) :
            x += diem[i]
        x /= 12
        if x < 5 : self.xeploai = 'YEU'
        elif x < 7 : self.xeploai = 'TB'

        elif x < 8 : self.xeploai = 'KHA'
        elif x < 9 : self.xeploai = 'GIOI'
        else : self.xeploai = 'XUAT SAC'
        self.diemTB = x.quantize(Decimal('0.1'), ROUND_HALF_UP)
    def output(self) :
        print(self.maHS, self.ten, self.diemTB, self.xeploai)

n = int(input())
a = []
for i in range(n) :
    b = input()
    c = [Decimal(x) for x in input().split()]
    a.append(HocSinh(b, c))
a = sorted(a, key = lambda x : (-x.diemTB, x.maHS))
for i in a :
    i.output()

