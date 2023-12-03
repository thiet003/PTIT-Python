gia ={
    'Xe_con5': 10000,
    'Xe_con7': 15000,
    'Xe_tai2': 20000,
    'Xe_khach29': 50000,
    'Xe_khach45': 70000
}
n = int(input())
thongke={}
for j in range(n):
    s=input().split(' ')
    loaixe=s[1]+s[2]
    ravao = s[3]
    ngay =s[4]
    x = 0
    if ngay in thongke:
        x=thongke[ngay]
    if ravao=="IN":
        thongke[ngay]=x+gia[loaixe]
for key,value in thongke.items():
    print(key+": "+str(value))