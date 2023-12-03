n = int(input())
deg  =[0]*100005
for i in range(n-1):
    x,y=[int(x) for x in input().split()]
    deg[x]+=1
    deg[y]+=1
dem1=0
dem2=0
for x in range(1,n+1):
    if deg[x]==n-1:
        dem1+=1
    elif deg[x]==1:
        dem2+=1
if dem1==1 and dem2==n-1:
    print("Yes")
else: print("No")