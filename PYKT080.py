def check(x,y,n,m):
    return x>=0 and x<n and y>=0 and y<m
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]
n,m = [int(x) for x in input().split()]
a = []
c = []
sum=0
for i in range(n):
    d = [0]*(m+5)
    c.append(d)
    b = [int(x) for x in input().split()]
    a.append(b)
for i in range(0,n):
    for j in range(0,m):
        if a[i][j]==-1:
            for k in range(8):
                x1=i+dx[k]
                y1=j+dy[k]
                if(not check(x1,y1,n,m)):
                    continue
                if(c[x1][y1]==0):
                    sum+=a[x1][y1]
                    c[x1][y1]=1
print(sum)

