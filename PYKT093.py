from math import ceil
def chuanhoa(s):
    ds = s.strip().lower().split()
    ans=""
    ans+=ds[0][:1].upper()+ds[0][1:]
    for i in range(1,len(ds)):
        ans+=" "
        ans+=ds[i][:1].upper()+ds[i][1:]
    return ans
        
class SV:
    def __init__(self,ma,ten,diem1,diem2,diem3) -> None:
        self.ma = "SV"+format(ma,"02d")
        self.ten = chuanhoa(ten)
        self.tb = float((diem1*3+diem2*3+diem3*2)/8);
        self.xh = 0
    def setXH(self,x):
        self.xh = x
    def __str__(self) -> str:
        return f'{self.ma} {self.ten} {(ceil(self.tb*100)/100):.2f} {str(self.xh)}'
n = int(input())
e = []
for i in range(n):
    e.append(SV(i+1,input(),float(input()),float(input()),float(input())))
e = sorted(e,key=lambda x: -x.tb)
dem=1
for i in range(len(e)):
    if i==0:
        e[i].setXH(1)
    elif e[i].tb == e[i-1].tb:
        e[i].setXH(e[i-1].xh)
    else:
        e[i].setXH(dem)
    print(e[i])
    dem+=1
