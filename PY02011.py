from math import fabs
n = int(input())
b=[int(x) for x in input().split()]
b.append(0)
a=sorted(b)
sum=[0]*(n+5)
# for x in a:
#     print(x,end=" ")
# print()
for i in range(len(a)):
    if i==0: sum[i]=a[i]
    else: sum[i]=sum[i-1]+a[i]
e=[]
ans=1e9
for i in range(1,len(a)):
    x=(i-1)*a[i]-sum[i-1]+sum[len(a)-1]-sum[i]-(len(a)-i-1)*a[i]
    if ans>x:
        ans=x
        e.clear()
        e.append(a[i])
    elif ans==x:
        e.append(a[i])
for i in b:
    if i in e:
        print(ans,i)
        break