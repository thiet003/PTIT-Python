class GV:
    def __init__(self,ma,ten,maxet,tin,chuyenmon) -> None:
        self.ma = "GV"+format(ma,"02d")
        self.ten = ten 
        self.maxet = maxet
        self.tin = tin
        self.chuyenmon = chuyenmon
        uutien =0
        x=maxet[1]
        z=maxet[0]
        if z=="A": self.mon = "TOAN"
        if z=="B": self.mon = "LY"
        if z=="C": self.mon = "HOA"
        if x=="1": uutien =2.0
        if x=="2": uutien =1.5
        if x=="3": uutien =1.0
        self.tong = tin*2+chuyenmon+uutien;
        if self.tong>=18:
            self.tt = "TRUNG TUYEN"
        else: self.tt = "LOAI"
    def __str__(self) -> str:
        return f'{self.ma} {self.ten} {self.mon} {str(self.tong)} {self.tt}'
n = int(input())
e = []
for l in range(n):
    e.append(GV(l+1,input().strip(),input().strip(),float(input()),float(input())))
e = sorted(e,key=lambda s: s.tong,reverse=True)
for x in e:
    print(x)