t = int(input())
e=[]
while True:
    try:
        e.extend(map(int,input().split()))     
    except:
        break
x=0
for l in range(t):
    n=e[x]
    m=e[x+1]
    x+=2
    a = []
    for i in range(n): a.append([0]*m)
    while len(e) - x < n*m: e.append(0)
    for i in range(n):
        for j in range(m): a[i][j] = e[x+j]
        x+=m
    b = []
    for i in range(m):
        d=[]
        for j in range(n):
            d.append(a[j][i])
        b.append(d)
    res=[]
    for i in range(n): res.append([0]*n)
    for i in range(n):
        for j in range(n):
            res[i][j]=0
            for k in range(m):
                res[i][j]+=(a[i][k]*b[k][j])
    for i in range(n):
        for j in range(n):
            print(res[i][j],end=" ")
        print()