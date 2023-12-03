from datetime import datetime
def par_ngay(s):
    return datetime.strptime(s,"%d/%m/%Y")
def par_gio(s):
    return datetime.strptime(s,"%H:%M")
mh={}
class Lich:
    def __init__(self,ma,ten,ngay,gio,nhom) -> None:
        self.ma = "T"+format(ma,"03d")
        self.ten = ten
        self.ngay = ngay
        self.gio = gio
        self.nhom = nhom
    def out(self):
        print(self.ma + " "+self.ten+" "+mh[self.ten]+" "+self.ngay+" "+self.gio+" "+self.nhom)
n,m = map(int,input().split())
for j in range(n):
    x=input()
    y=input()
    mh[x]=y
e = []
for j in range(m):
    x=input().split()
    e.append(Lich(j+1,x[0],x[1],x[2],x[3]))
e = sorted(e, key = lambda x: (par_ngay(x.ngay),par_gio(x.gio),x.ma))
for x in e:
    x.out()