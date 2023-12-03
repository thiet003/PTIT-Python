import math
t = int(input())
for j in range(t):
    n,m = map(int, input().split())
    a=[int(x) for x in input().split()]
    ok=0
    maxx=-1e10
    b=[]
    for x in a:
        maxx=max(maxx,x)
    for x in a:
        if(ok==0 and x==maxx):
            ok=1
            b.append(m)
        b.append(x)
    c=[]
    d=[]
    for x in b:
        if x<0:
            c.append(x)
        else:
            d.append(x)
    for x in c:
        print(x,end=' ')
    for x in d:
        print(x,end=' ')
    print()
