
x={}
y={}
class Team:
    def __init__(self,ma,ten,nh) -> None:
        self.ma = "C"+format(ma,"03d")
        self.ten = ten
        self.kh = x[nh]
        self.truong = y[nh]
    def __str__(self) -> str:
        return f'{self.ma} {self.ten} {self.kh} {self.truong}'
n = int(input())
for i in range(n):
    ma = "Team"+format(i+1,"02d")
    x[ma]=input()
    y[ma]=input()
m = int(input())
e = []
for i in range(m):
    e.append(Team(i+1,input(),input()))
e = sorted(e,key=lambda x: x.ten)
for xx in e:
    print(xx)