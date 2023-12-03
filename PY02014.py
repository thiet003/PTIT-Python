from math import sqrt
def sang(a):
    for i in range(1,10001):
        a[i]=1
    a[0]=0
    a[1]=0
    for i in range(2,int(sqrt(10001)+1)):
        if(a[i]==1):
            for j in range(i*i,10001,i):
                a[j]=0           
n=int(input())
a=[0]*10001
sang(a)
c=[int(x) for x in input().split()]
ans=0
for i in range(n):
    if a[c[i]]==1:
        continue
    x=0
    for j in range(c[i]-1,0,-1):
        if a[j]==1:
            x=c[i]-j
            break
    y=0
    for j in range(c[i]+1,10001):
        if a[j]==1:
            y=j-c[i]
            break
    ans=max(ans,min(x,y))
print(ans)