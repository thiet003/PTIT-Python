import math
class Point:
    def __init__(self,x,y):
        self.x = x;
        self.y = y;
    def distance(self, tmp):
        xx=(tmp.x - self.x)**2;
        yy=(tmp.y - self.y)**2;
        zz = float(math.sqrt(xx+yy))
        return zz
class Triangle:
    def __init__(self,x,y,z):
        self.x = x;
        self.y = y;
        self.z = z;
    def cal(self):
        xx = self.x.distance(self.y);
        yy = self.y.distance(self.z);
        zz = self.z.distance(self.x);
        res=float(xx+yy+zz)
        if xx+yy<=zz or yy+zz<=xx or xx+zz<=yy:
            return "INVALID"
        else:
            return format(res,".3f")

t = int(input())
arr=[]
i=0
for j in range(t):
    arr.extend([float(x) for x in input().split()])
for j in range(t):
    res = Triangle(Point(arr[i],arr[i+1]),Point(arr[i+2],arr[i+3]),Point(arr[i+4],arr[i+5]))
    i+=6
    print(res.cal())