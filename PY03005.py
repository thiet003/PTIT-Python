import re
n,k = [int(x) for x in input().split()]
e = {}
for i in range(n):
    s = input()
    ds = re.split(r'[^a-z0-9]',s.lower());
    for x in ds:
        if x=="":
            continue;
        if x in e:
            e[x]=e[x]+1
        else: e[x]=1
e = sorted(e.items(),key=lambda x: (-x[1],x[0]))
e = dict(e)
for x in e.keys():
    if e[x]>=k:
        print(x,e[x])
