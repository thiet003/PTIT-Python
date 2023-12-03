import math
def nto(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return n>1
n = int(input())
a =[int(x) for x in input().split()]
d=[0]*(n+5)
b=[]
for i in range(n):
    if nto(a[i]):
        d[i]=1
        b.append(a[i])
b.sort()
j=0
for i in range(n):
    if d[i]==1:
        print(b[j],end=" ")
        j+=1
    else: print(a[i],end=" ")