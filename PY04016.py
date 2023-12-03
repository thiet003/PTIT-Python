from datetime import datetime
def getNgay(st,en):
    format = "%d/%m/%Y"
    s_st = datetime.strptime(st,format).date()
    s_en = datetime.strptime(en,format).date()
    res = (s_en-s_st).days+1
    return res
class HoaDon:
    def __init__(self,ma,ten,sophong,nhan,tra,tienDV) -> None:
        self.ma = "KH"+format(ma,"02d")
        self.ten = ten.strip()
        self.sophong = sophong
        self.songayo = getNgay(nhan.strip(),tra.strip())
        tang = int(sophong[0])
        if(tang==1):
            self.tong = 25*self.songayo + tienDV
        elif(tang==2):
            self.tong = 34*self.songayo + tienDV
        elif(tang==3):
            self.tong = 50*self.songayo + tienDV
        elif(tang==4):
            self.tong = 80*self.songayo + tienDV
    def out(self):
        print(f'{self.ma} {self.ten} {str(self.sophong)} {str(self.songayo)} {str(self.tong)}')
n = int(input())
e = []
for l in range(n):
    e.append(HoaDon(l+1,input(),input(),input(),input(),int(input())))
e =sorted(e,key=lambda s: s.tong,reverse=True)
for x in e:
    x.out()
