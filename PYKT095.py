def chuanhoa(s):
    ds=s.strip().lower().split()
    ans=""
    ans+=ds[0][0].upper()+ds[0][1:]
    for i in range(1,len(ds)):
        ans+=" "
        ans+=ds[i][0].upper()+ds[i][1:]
    return ans
class KH:
    def __init__(self,ma,ten,loai,dau,cuoi) -> None:
        self.ma = "KH"+format(ma,"02d")
        self.ten = chuanhoa(ten)
        if loai=="A":
            self.dm=100
        if loai=="B":
            self.dm=500
        if loai=="C":
            self.dm=200
        sodien = cuoi-dau
        if sodien<self.dm:
            self.tdm = sodien*450
            self.vdm = 0
            self.vat = 0
        else:
            self.tdm = self.dm*450
            self.vdm = (sodien-self.dm)*1000
            self.vat = self.vdm//20
        self.tien = self.tdm + self.vdm + self.vat
    def __str__(self) -> str:
        return f'{self.ma} {self.ten} {str(self.tdm)} {str(self.vdm)} {str(self.vat)} {str(self.tien)}'
n = int(input())
e = []
for i in range(n):
    s = input()
    ds = input().split()
    e.append(KH(i+1,s,ds[0],int(ds[1]),int(ds[2])))
e = sorted(e, key=lambda x: (-x.tien))
for x in e:
    print(x)