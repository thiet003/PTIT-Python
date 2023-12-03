class BXH:
    def __init__(self,ten,ac,sm) -> None:
        self.ten = ten
        self.ac = ac
        self.sm = sm
    def out(self):
        print(self.ten + " "+str(self.ac)+" "+str(self.sm))
n = int(input())
e=[]
for j in range(n):
    s=input()
    x,y=map(int,input().split())
    e.append(BXH(s,x,y))
e = sorted(e, key=lambda x: (-x.ac,x.sm,x.ten))
for x in e:
    x.out()