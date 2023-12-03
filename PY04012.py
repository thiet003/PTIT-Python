class CC:
    def __init__(self,ma,ten,lop) -> None:
        self.ma = ma
        self.ten = ten
        self.lop = lop
        self.diem = 0
        self.trangThai = ""
    def setDiem(self,diem):
        self.diem = diem
    def out(self):
        print(f'{self.ma} {self.ten} {self.lop} {self.diem}',end="")
        if(self.diem==0):
            print(" KDDK",end="")
        print()
n = int(input())
e=[]
cc = {}
dd = {}
for l in range(n):
    e.append(CC(input(),input(),input()))
for l in range(n):
    x=10
    ma,tt = input().split()
    for j in tt:
        if j=="v":
            x-=2
        if j=="m":
            x-=1
    if x<0: x=0
    dd[ma]=x
for x in e:
    x.setDiem(dd[x.ma])
for x in e:
    x.out();

