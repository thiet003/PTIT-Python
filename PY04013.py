from datetime import datetime
def calTime(st,en):
    format = "%H:%M"
    t_st = datetime.strptime(st,format)
    t_end = datetime.strptime(en,format)
    delta = t_end-t_st
    return float(delta.total_seconds()/3600)
class LuongMua:
    def __init__(self,id,ten,luongmua) -> None:
        self.ma = "T"+format(id,"02d")
        self.ten = ten
        self.luongmua = luongmua
    def out(self):
        print(str(self.ma)+" "+self.ten+" "+str(format(self.luongmua,".2f")))
t = int(input())
thoigian = {}
lm = {}
for l in range(t):
    ten = input()
    st = input()
    en = input()
    sl = int(input())
    if ten in thoigian:
        x = thoigian[ten]
        thoigian[ten]=x+calTime(st,en)
        y = lm[ten]
        lm[ten]=y+sl
    else:
        thoigian[ten]=calTime(st,en)
        lm[ten]=sl
a=[]
id=1
for x in thoigian.keys():
    a.append(LuongMua(id,x,float(lm[x]/thoigian[x])))
    id+=1
for x in a:
    x.out()
        