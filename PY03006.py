import re
def ch(s):
    ans=""
    for x in s:
        if str(x).isdigit():
            continue
        ans+=str(x)
    return ans;

n = int(input())
e = {}
for i in range(n):
    s = input()
    ds = re.split(r'[^a-z0-9]',s.lower());
    for x in ds:
        x=ch(x)
        if x=="":
            continue;
        if x in e:
            e[x]=e[x]+1
        else: e[x]=1
e = sorted(e.items(),key=lambda x: (-x[1],x[0]))
e = dict(e)
for x in e.keys():
    print(x,e[x])
