from datetime import datetime
def calTime(st,en):
    format = "%H:%M"
    t_st = datetime.strptime(st,format)
    t_en = datetime.strptime(en,format)
    res = (t_en-t_st).total_seconds()
    gio = int(res//3600)
    phut = int((res%3600)//60)
    return gio,phut,f'{gio} gio {phut} phut'
class Choi:
    def __init__(self,ma,ten,st,en) -> None:
        self.ma = ma 
        self.ten = ten
        self.gio,self.phut,self.time = calTime(st,en)
    def out(self):
        print(self.ma +" "+self.ten+" "+self.time)
n = int(input())
e=[]
for l in range(n):
    e.append(Choi(input(),input(),input(),input()))
e = sorted(e,key=lambda s: (-s.gio,-s.phut))
for x in e:
    x.out() 