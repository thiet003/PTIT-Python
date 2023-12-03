def dfs(u,vs):
    vs[u]=1
    for v in adj[u]:
        if vs[v]==0:
            dfs(v,vs)
n,m,u = [int(x) for x in input().split()]
adj = {x:[] for x in range(1,n+1)}
vs = [0]*500
for j in range(m):
    x,y=[int(x) for x in input().split()]
    adj[x].append(y)
    adj[y].append(x)
dem=0
dfs(u,vs)
for x in range(1,n+1):
    if vs[x]==0: print(x)