from math import sqrt
def nto(n):
    for i in range(2,int(sqrt(n))+1):
        if n %i==0: return False
    return n>1
n,m = map(int, input().split())
a=[]
for i in range(n):
    a.append([int(x) for x in input().split()])
ans=0
ok=0
for i in range(n):
    for j in a[i]:
        if nto(j):
            ok=1
            if j > ans:
                ans=j
if ok==0:
    print("NOT FOUND")
else:
    print(ans)
    for i in range(n):
        for j in range(m):
            if a[i][j]==ans:
                print(f'Vi tri [{i}][{j}]')