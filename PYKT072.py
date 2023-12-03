n = int(input())
a=[]
for l in range(n):
    a.append(input())
ans=1e9
dem=len(a[0])
ok=1
for i in range(1,n):
    if len(a[i])!=dem:
        ok=0
if ok==0:
    print("-1")
else:
    for i in a:
        xi=0
        for j in a:
            x = 0
            okk=0
            while x <= len(i):
                if i==j:
                    xi+=x
                    okk=1
                    break
                j = j[1:]+j[0]
                x+=1
            if okk==0:
                ok=0
                break
        ans=min(ans,xi)
    if ok==0:
        print(-1)
    else: print(ans)