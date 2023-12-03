from math import sqrt
def nto(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0: return False
    return n>1
n = int(input())
a = [int(x) for x in input().split()]
b=[]
b.append(0)
for i in a:
    if i not in b:
        b.append(i)
sum = [0]*(n+5)
sum[0]=0
for i in range(1,len(b)):
    sum[i]=sum[i-1]+b[i]
ok=1
for i in range(1,len(b)):
    if nto(sum[i]-sum[0]) and nto(sum[len(b)-1]-sum[i]):
        print(i-1)
        ok=0
        break
if ok==1: print("NOT FOUND")