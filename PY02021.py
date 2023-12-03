t = int(input())
for j in range(t):
    n,m,k = [int(x) for x in input().split()]
    a=[int(x) for x in input().split()]
    b=[int(x) for x in input().split()]
    c=[int(x) for x in input().split()]
    x=0
    y=0
    z=0
    dem=0
    while x<n and y<m and z<k:
        if(a[x]==b[y] and b[y]==c[z]):
            print(a[x],end=" ")
            dem+=1
            x+=1
            y+=1
            z+=1
        elif(a[x]<=b[y] and a[x]<=c[z]):
            x+=1
        elif(a[x]>=b[y] and b[y]<=c[z]):
            y+=1
        else:
            z+=1
    if(dem==0): print("NO")
    else: print()