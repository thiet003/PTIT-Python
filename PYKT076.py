from datetime import datetime

# Hàm chuyển đổi chuỗi ngày thành đối tượng datetime
def parse_date(date_string):
    return datetime.strptime(date_string, '%d/%m/%Y')

class TheLoai:
    def __init__(self,ma,ten) -> None:
        self.ma = "TL"+format(ma,"03d")
        self.ten = ten
tl = {}
class Phim:
    def __init__(self,ma,theloai,ngay,ten,sotap) -> None:
        self.ma = "P"+format(ma,"03d")
        self.theloai=tl[theloai]
        self.ngay = ngay
        self.ten = ten
        self.sotap = sotap
    def out(self):
        print(self.ma+" "+self.theloai+" "+self.ngay+" "+self.ten+" "+str(self.sotap))
n,m = [int(x) for x in input().split()]
for j in range(n):
    x = TheLoai(j+1,input())
    tl[x.ma]=x.ten
e = []

for j in range(m):
    e.append(Phim(j+1,input(),input(),input(),int(input())))
e = sorted(e,key=lambda s: (parse_date(s.ngay),s.ten,-s.sotap))
for x in e:
    x.out()