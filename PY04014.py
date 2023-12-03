class DiemSo:
    def __init__(self,ma,ten,diem) -> None:
        self.ma = "HS"+format(ma,"02d")
        self.ten = ten
        self.diem = diem
        if diem>=9:
            self.loai = "XUAT SAC"
        elif diem>=8:
            self.loai = "GIOI"
        elif diem>=7:
            self.loai = "KHA"
        elif diem>=5:
            self.loai = "TB"
        else:
            self.loai = "YEU"
    def out(self):
        x = round(self.diem+1e-10,1)
        print(str(self.ma)+" "+self.ten+" "+str(x)+" "+self.loai)
n = int(input())
e=[]
for l in range(n):
    ten = input()
    a=[float(x) for x in input().split()]
    diem =a[0]*2+a[1]*2
    for k in range(2,10):
        diem+=a[k]
    diem = float(diem/12)
    e.append(DiemSo(l+1,ten,diem))
e = sorted(e,key=lambda s: s.diem, reverse=True)
for x in e:
    x.out()