t = int(input())
for l in range(t):
    n,m=[int(x) for x in input().split()]
    a=[]
    b=[]
    res=[]
    for i in range(n):
        c=[0]*n
        res.append(c)
        d=[int(x) for x in input().split()]
        a.append(d)
    for i in range(m):
        d=[]
        for j in range(n):
            d.append(a[j][i])
        b.append(d)
    for i in range(n):
        for j in range(n):
            res[i][j]=0
            for k in range(m):
                res[i][j]+=(a[i][k]*b[k][j])
    for i in range(n):
        for j in range(n):
            print(res[i][j],end=" ")
        print()