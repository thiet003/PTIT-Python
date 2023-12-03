from math import fabs
class SoPhuc:
    def __init__(self,thuc,ao) -> None:
        self.thuc = thuc
        self.ao = ao
    def cong(self,b):
        thuc = self.thuc + b.thuc
        ao = self.ao + b.ao
        return SoPhuc(thuc,ao)
    def nhan(self,b):
        thuc = self.thuc * b.thuc - self.ao * b.ao
        ao = self.thuc * b.ao + self.ao * b.thuc
        return SoPhuc(thuc,ao)
    def out(self):
        print(self.thuc,end=" ")
        if self.ao < 0:
            print("-",end=" ")
        else:
            print("+",end=" ")
        print(str(int(fabs(self.ao)))+"i")
    def out2(self):
        print(self.thuc,end=" ")
        if self.ao < 0:
            print("-",end=" ")
        else:
            print("+",end=" ")
        print(str(int(fabs(self.ao)))+"i, ",end="")


t = int(input())
for l in range(t):
    a,b,c,d = map(int, input().split())
    x = SoPhuc(a,b)
    y = SoPhuc(c,d)
    z = x.nhan(x.cong(y))
    w = x.cong(y)
    ww = w.nhan(w)
    z.out2()
    ww.out()