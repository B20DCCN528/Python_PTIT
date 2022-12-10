class Matrix:
    def __init__(self, n, m, arr):
        self.n = n
        self.m = m
        self.arr = arr
    def mul(self):
        for i in range(self.n):
            for j in range(self.n):
                tmp = 0
                for k in range(self.m):
                    tmp += (self.arr[i][k]*self.arr[j][k])
                print(tmp, end=" ")
            print()

for i in range(int(input())):
    n, m = map(int,input().split())
    arr = []
    for j in range(n):
        arr.append([int(x) for x in input().split()])
    matrix = Matrix(n, m, arr)
    matrix.mul()