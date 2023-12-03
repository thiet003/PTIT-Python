
def dfs(e,u,v,adj):
    vs = [0]*105
    q=[u]
    vs[u]=1
    while len(q)>0:
        x = q.pop()
        if(x==v): return False
        for i in adj[x]:
                if(vs[i]==0 and i!=e):
                    q.append(i)
                    vs[i]=1

    return True

t = int(input())
for l in range(t):
    n,m,u,v = [int(x) for x in input().split()]
    adj = {x:[] for x in range(1,n+1)}
    for i in range(m):
        x,y = [int(r) for r in input().split()]
        adj[x].append(y)
    dem=0
    for i in range(1,n+1):
        if(i!=u and i!=v):
            if(dfs(i,u,v,adj)): 
                dem+=1
    print(dem)