class Thi:
    def __init__(self,ma,ten,lt,th) -> None:
        self.ma = "TS0"+str(ma)
        self.ten = ten
        self.tb = float((lt+th)/2)
        if self.tb >= 9.5:
            self.loai = "XUAT SAC"
        elif self.tb >=8:
            self.loai = "DAT"
        elif self.tb >=5:
            self.loai = "CAN NHAC"
        else:
            self.loai = "TRUOT"
    def out(self):
        x = round(self.tb,2)
        print(str(self.ma)+" "+self.ten +" "+str(format(x,".2f"))+" "+self.loai)
n = int(input())
e=[]
for l in range(n):
    ten = input()
    lt = float(input())
    if lt>10:
        lt = lt/10
    th = float(input())
    if th>10:
        th = th/10
    e.append(Thi(l+1,ten,lt,th))
e = sorted(e,key=lambda s: s.tb, reverse=True)
for x in e:
    x.out()
