n,m=map(int, input().split())
a=[]
for i in range(n):
    a.append([int(i) for i in input().split()])
b = []
if n>m:
    dem=0
    for i in range(1,n-m+1):
        b.append(dem)
        dem+=2
    for i in range(n):
        if i in b:
            continue
        for j in range(m):
            print(a[i][j],end=" ")
        print()
elif n<=m:
    dem=1
    for i in range(1,m-n+1):
        b.append(dem)
        dem+=2
    for i in range(n):
        ok=1
        for j in range(m):
            if j in b:
                ok=0
                continue
            print(a[i][j],end=" ")
        print()