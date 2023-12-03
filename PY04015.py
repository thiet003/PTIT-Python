class HoaDon:
    def __init__(self,ma,ten,cu,moi) -> None:
        self.ma = "KH"+format(ma,"02d")
        self.ten = ten
        res = moi - cu
        if(res<=50):
            self.tien = res*102
        elif(res<=100):
            self.tien = round((5000 + (res-50)*150)/100*103)
        else:
            self.tien = round((12500 + (res-100)*200)/100*105)
    def out(self):
        print(str(self.ma)+" "+self.ten+" "+str(self.tien))
n = int(input())
e=[]
for l in range(n):
    ten = input()
    cu =int(input())
    moi =int(input())
    e.append(HoaDon(l+1,ten,cu,moi))
e = sorted(e,key=lambda s: s.tien, reverse=True)
for x in e:
    x.out()