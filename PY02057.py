from math import sqrt
def nto(n):
    if n<10: return False
    n=str(n)
    return n == n[::-1]
n,m = map(int, input().split())
a=[]
for i in range(n):
    a.append([int(x) for x in input().split()])
ans=0
minn=1e9
maxx=-1e9
for i in range(n):
    for j in a[i]:
        minn=min(minn,j)
        maxx=max(maxx,j)
ans = int(maxx-minn)
ok=0
for i in range(n):
    for j in range(m):
            if a[i][j]==ans:
                ok=1
if ok==0:
    print("NOT FOUND")
else:
    print(ans)
    for i in range(n):
        for j in range(m):
            if a[i][j]==ans:
                print(f'Vi tri [{i}][{j}]')