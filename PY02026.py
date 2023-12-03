n,m=[int(x) for x in input().split()]
a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
mp1={}
mp2={}
for i in a:
    mp1[i]=1
for i in b:
    mp2[i]=1
c = []
d = []
for i in mp1.keys():
    c.append(i)
for i in mp2.keys():
    d.append(i)
c.sort()
d.sort()
if len(c)!=len(d):
    print("NO")
else:
    ok=1
    for i in range(len(c)):
        if c[i]!=d[i]:
            print("NO")
            ok=0
            break
    if ok==1:
        print("YES")