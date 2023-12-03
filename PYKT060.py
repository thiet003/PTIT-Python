def dfs(u,vs):
    vs[u]=1
    for v in adj[u]:
        if vs[v]==0:
            dfs(v,vs)
n = int(input())
m = int(input())
adj = {x:[] for x in range(1,n+1)}
vs = []
vss=[0]*1005
for i in range(0,1005):
    vs.append([0]*1005)
for j in range(m):
    x,y=[int(x) for x in input().split()]
    vs[x][y]=1
    vs[y][x]=1
for j in range(1,n+1):
    for k in range(j+1,n+1):
        if vs[j][k]==0:
            adj[j].append(k)
            adj[k].append(j)
dem=0
dfs(1,vss)
for x in range(1,n+1):
    if vss[x]==0: dem+=1
if dem==0:
    print("YES")
else: print("NO")