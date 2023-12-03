def gcd(a,b):
    if(b==0):
        return a
    return gcd(b,a%b)
class PhanSo:
    def __init__(self,tu,mau) -> None:
        self.tu = tu
        self.mau = mau
    def add(self, tmp):
        tu = self.tu * tmp.mau + self.mau * tmp.tu;
        mau = self.mau * tmp.mau
        l = gcd(tu,mau)
        tu = tu // l
        mau = mau // l
        print(str(tu)+"/"+str(mau))
    def out(self):
        l = gcd(self.tu,self.mau)
        self.tu = self.tu//l
        self.mau = self.mau//l
        print(str(self.tu)+'/'+ str(self.mau))

a,b,c,d = map(int,input().split())
x = PhanSo(a,b)
y = PhanSo(c,d)
x.add(y)