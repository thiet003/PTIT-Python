t = int(input())
for j in range(t):
    n = int(input())
    a=[int(x) for x in input().split()]
    b=[int(x) for x in input().split()]
    a.sort()
    b.sort()
    ok = True;
    for i in range(n):
        if(a[i]>b[i]):
            ok=False
            break
    if ok:
        print("YES")
    else:
        print("NO")