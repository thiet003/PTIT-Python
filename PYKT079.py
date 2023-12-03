t = int(input())
for j in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    maxx=-1e4
    minn=1e4
    for x in a:
        maxx=max(maxx,x)
        minn=min(minn,x)
    s = set(a)
    print(maxx-minn+1-len(s))