n = int(input())
a=[]
while True:
    try:
        a.extend(map(int,input().split()))
    except:
        break
b=[]
c=[]
d=[0]*(1005)
for i in range(n):
    if a[i]%2==0:
        # chan
        b.append(a[i])
        d[i]=0
    else:
        c.append(a[i])
        d[i]=1
b.sort()
c = sorted(c,reverse=True)
i=0
j=0
for k in range(n):
    if d[k]==0:
        print(b[i],end=" ")
        i+=1
    else:
        print(c[j],end=" ")
        j+=1
