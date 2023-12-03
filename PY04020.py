class CH:
    def __init__(self,ma,ten,sl,gia,chiet) -> None:
        self.ma = ma
        self.ten = ten
        self.sl = sl
        self.gia = gia
        self.chiet = chiet
        self.tong = sl*gia -chiet
    def __str__(self) -> str:
        return f'{self.ma} {self.ten} {self.sl} {self.gia} {self.chiet} {self.tong}'
n = int(input())
e = []
for l in range(n):
    e.append(CH(input(),input(),int(input()),int(input()),int(input())))
e = sorted(e,key=lambda s: s.tong,reverse=True)
for x in e:
    print(x)