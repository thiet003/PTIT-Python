phongban = {}
class NV:
    def __init__(self,ma,ten,luong,ngay) -> None:
        self.ma = ma 
        self.ten = ten
        self.pb = phongban[ma[-2:]]
        x = ma[0]
        y=int(ma[1]+ma[2])
        if y>=1 and y<=3:
            if x=="A": self.hs = 10
            if x=="B": self.hs = 10
            if x=="C": self.hs = 9
            if x=="D": self.hs = 8
        elif y<=8:
            if x=="A": self.hs = 12
            if x=="B": self.hs = 11
            if x=="C": self.hs = 10
            if x=="D": self.hs = 9
        elif y<=15:
            if x=="A": self.hs = 14
            if x=="B": self.hs = 13
            if x=="C": self.hs = 12
            if x=="D": self.hs = 11
        else:
            if x=="A": self.hs = 20
            if x=="B": self.hs = 16
            if x=="C": self.hs = 14
            if x=="D": self.hs = 13
        self.tien = (luong*ngay)*self.hs*1000
    def __str__(self) -> str:
        return f'{self.ma} {self.ten} {self.pb} {str(self.tien)}'
n = int(input())
for i in range(n):
    ds=input().split()
    ans=""
    for j in range(1,len(ds)):
        ans+=ds[j]
        if j!=len(ds)-1:
            ans+=" "
    phongban[ds[0]]=ans
e = []
m = int(input())
for i in range(m):
    e.append(NV(input(),input(),int(input()),int(input())))
for x in e:
    print(x)
