x=0
b=[]
def inn(n):
    dem=0
    for i in range(1,n+1):
        if(a[i]==2):
            dem+=1
    s=""
    if(dem/n>0.5 and a[1]!=0):
        for i in range(1,n+1):
            s+=str(a[i])
        b.append(s)
a=[0]*1000
def Try(i,n):
    for j in range(0,3):
        a[i]=j
        if(i==n):
            inn(n)
        else:
            Try(i+1,n)
t = int(input())
for j in range(t):
    cnt=0
    x = int(input())
    for i in range(1,10):
        Try(1,i)
    for i in range(x):
        print(b[i],end=' ')
    print()
