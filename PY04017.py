from datetime import datetime
def calTime(st,en):
    format = "%H:%M"
    t_st = datetime.strptime(st,format)
    t_en = datetime.strptime(en,format)
    res = t_en-t_st
    return float(res.total_seconds()/3600)
class Dua:
    def __init__(self,ten,donvi,time) -> None:
        self.ten = ten.strip()
        self.donvi = donvi.strip()
        ds1=donvi.split()
        x=""
        for r in ds1: x+=r[0].upper()
        ds2=ten.split()
        for r in ds2: x+=r[0].upper()
        self.ma = x
        self.tb = 120/calTime("6:00",time.strip())
    def out(self):
        print(f'{self.ma} {self.ten} {self.donvi} {str(round(self.tb))} Km/h')
n = int(input())
e = []
for l in range(n):
    e.append(Dua(input(),input(),input()))
e = sorted(e,key=lambda s: s.tb,reverse=True)
for x in e:
    x.out()
