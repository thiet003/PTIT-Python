class CaThi:
    def __init__(self,ma,ngay,gio,phong) -> None:
        self.ma = "C"+format(ma,"03d")
        self.ngay = ngay
        self.ngays = int(ngay[0:2])
        self.thangs = int(ngay[3:5])
        self.nams = int(ngay[6:])
        self.gio = gio
        self.gios = int(gio[0:2])
        self.phuts = int(gio[3:5])
        self.phong = phong
    def __str__(self) -> str:
        return f'{self.ma} {self.ngay} {self.gio} {self.phong}'
e = []
with open('CATHI.in','r') as file:
    n = int(file.readline())
    for i in range(n):
        e.append(CaThi(i+1,file.readline().strip(),file.readline().strip(),file.readline().strip()))
e = sorted(e,key=lambda x: (x.nams,x.thangs,x.ngays,x.gios,x.phuts,x.ma))
for i in e:
    print(i)