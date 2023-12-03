import re
res ={}
def ptich(res,s):
    ds = re.split(r'[^a-z0-9]+',s.lower())
    for x in ds:
        if x:
            if x in res:
                res[x]+=1
            else: res[x]=1
n = int(input())
for j in range(n):
    ptich(res,input())
res = sorted(res.items(), key=lambda x: (-x[1],x[0]))
res = dict(res)
for x in res.keys():
    print(x,res[x])