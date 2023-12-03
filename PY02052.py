from math import fabs
n = int(input())
a=[]
for i in range(n):
    a.append([int(x) for x in input().split()])
k = int(input())
tren,duoi=0,0
for i in range(n):
    for j in range(n):
        if i < j : duoi+=a[i][j]
        if i > j : tren+=a[i][j]
res = int(fabs(tren-duoi))
if res<=k:
    print("YES")
else:
    print("NO")
print(res)