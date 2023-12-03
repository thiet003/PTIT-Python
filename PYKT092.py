def chuanHoa(s):
    a = s.strip().split();
    x=a[0][:1].upper()+a[0][1:].lower()
    for i in range(1,len(a)):
        x+=" "
        x+=(a[i][:1].upper()+a[i][1:].lower())
    return x
class TS:
    def __init__(self,ma,ten,diem,dt,kv) -> None:
        self.ma = "TS"+format(ma,"02d")
        self.ten = chuanHoa(ten)
        self.dt = dt
        if kv==1: diem +=1.5
        if kv==2: diem +=1.0
        if dt != "Kinh": diem +=1.5
        self.diem = diem
        if diem >= 20.5: self.loai = "Do"
        else: self.loai = "Truot"
    def __str__(self) -> str:
        return f'{self.ma} {self.ten} {str(format(self.diem,".1f"))} {self.loai}'
    
n = int(input())
e = []
for j in range(n):
    e.append(TS(j+1,input(),float(input()),input(),int(input())))
e = sorted(e, key=lambda x: (-x.diem,x.ma))
for x in e:
    print(x)