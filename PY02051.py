n = int(input())
b=[]
s=0
summ=0
for i in range(n):
    arr= [int(x) for x in input().split()]
    summ+=sum(arr)
    if i ==0:
        s+=sum(arr)
    b.append(arr)
if n==1:
    print(0)
elif n==2:
    print(1,summ//2-1)
else:
    x=0
    sum2=0
    if n %2==0:
        for i in range(0,n-1,2):
            sum2+=b[i][i+1]
        x=(s-sum2)//(n-2)
    else:
        for i in range(1,n-1,2):
            sum2+=b[i][i+1]
        x=(s-sum2)//(n-1)
    print(x,end=" ")
    for i in range(1,n):
        print(b[0][i]-x,end=" ")
