def dfs(u,w,vs):
    vs[u]=1
    for v in adj[u]:
        if vs[v]==0 and v!=w:
            dfs(v,w,vs)
t = int(input())
for j in range(t):
    n,m = [int(x) for x in input().split()]
    vs=[0]*(n+5)
    adj={x:[] for x in range(n+5)}
    for i in range(m):
        x,y=[int(x) for x in input().split()]
        adj[x].append(y);
        adj[y].append(x);
    ans=1
    id=0
    for i in range(1,n+1):
        vs=[0]*(n+5)
        dem=0
        for k in range(1,n+1):
            if(vs[k]==0 and k!=i):
                dfs(k,i,vs)
                dem+=1
        # print(dem,end=" ")
        if dem>ans:
            ans=dem
            id=i
    print(id)
