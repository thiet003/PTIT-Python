import math
n = int(input())
a = []
for i in range(n):
    b = [int(x) for x in input().split()]
    a.append(b)
tren = 0
duoi = 0
k = int(input())
for i in range(n):
    for j in range(n):
        if(i+j<n-1):
            tren+=a[i][j]
        if(i+j>n-1):
            duoi+=a[i][j]

if(math.fabs(tren-duoi)<=k):
    print("YES")
else:
    print("NO")
print(int(math.fabs(tren-duoi)))