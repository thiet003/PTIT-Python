def gcd(a,b):
    if(b==0):
        return a
    return gcd(b,a%b)
class PhanSo:
    def __init__(self,tu,mau) -> None:
        self.tu = tu
        self.mau = mau
    def out(self):
        l = gcd(self.tu,self.mau)
        self.tu = self.tu//l
        self.mau = self.mau//l
        print(str(self.tu)+'/'+ str(self.mau))

a,b = map(int,input().split())
x = PhanSo(a,b)
x.out()