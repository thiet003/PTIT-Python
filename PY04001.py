from decimal import Decimal
import math
class Point:
    def __init__(self,x,y):
        self.x = x;
        self.y = y;
    def distance(self, tmp):
        xx=(tmp.x - self.x)**2;
        yy=(tmp.y - self.y)**2;
        zz = float(math.sqrt(xx+yy))
        return format(zz,".4f")
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1