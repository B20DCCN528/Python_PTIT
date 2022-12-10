class Student:
    def __init__(self, id, name, p1, p2):
        self.id = id
        self.name = name
        self.p1 = p1 if p1 <= 10 else p1/10
        self.p2 = p2 if p2 <= 10 else p2/10
        self.average = (self.p1 + self.p2)/2
        self.rating = ""
    def xh(self):
        if self.average > 9.5: self.rating = "XUAT SAC"
        elif self.average >= 8: self.rating = "DAT"
        elif self.average >= 5: self.rating = "CAN NHAC"
        else: self.rating = "TRUOT"

    def __str__(self):
        return self.id + " " + self.name + " " + '%.2f'%self.average + " " + self.rating
data = list()
for i in range(int(input())):
    stu = Student('TS0%d'%(i+1), input(), float(input()), float(input()))
    stu.xh()
    data.append(stu)
data = sorted(data, key=lambda x : -x.average)
for i in data:
    print(i)