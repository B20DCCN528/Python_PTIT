import datetime

class Time:
    def __init__(self, id, name, time_in, time_out):
        self.id = id
        self.name = name
        self.time_in = time_in
        self.time_out = time_out
    def time_play(self):
        time_in = datetime.datetime.strptime(self.time_in, '%H:%M')
        time_out = datetime.datetime.strptime(self.time_out, '%H:%M')
        self.time = time_out - time_in
    def result(self):
        self.time = str(self.time)
        print(self.id, self.name, end = "")
        a = [int(i) for i in self.time.split(":")]
        print(' {} gio {} phut'.format(a[0], a[1]))
res = []
for i in range(int(input())):
    per = Time(input(), input(), input(), input())
    per.time_play()
    res.append(per)
res.sort(key=lambda x : x.time, reverse=True)
for i in res:
    i.result()