import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, Point):
        dist = math.sqrt((self.x - Point.x)**2+(self.y-Point.y)**2)
        return round(dist, 3)
    def Triangle(self, p2, p3):
        e1 = self.distance(p2)
        e2 = p2.distance(p3)
        e3 = self.distance(p3)
        if e1+e2>e3 and e2+e3>e1 and e1+e3>e2:
            return '{:.3f}'.format(e1+e2+e3)
        else:
            return 'INVALID'
t = int(input())
while t > 0:
    t -= 1
    a = [float(x) for x in input().split()]
    p1 = Point(a[0], a[1])
    p2 = Point(a[2], a[3])
    p3 = Point(a[4], a[5])
    print(p1.Triangle(p2, p3))