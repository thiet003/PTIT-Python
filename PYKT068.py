class Thi:
    def __init__(self,ma,ten,ht) -> None:
        self.ma = ma 
        self.ten = ten
        self.ht = ht
    def __str__(self) -> str:
        return f'{self.ma} {self.ten} {self.ht}'
        
n = int(input())
e = []
for j in range(n):
    e.append(Thi(input(),input(),input()))

e = sorted(e,key=lambda x: x.ma)
for x in e:
    print(x)