n = int(input())
a = []
while len(a)<n:
    a.extend(list(map(int, input().split())))
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if(a[i]%2==0 and a[j]%2==0 and a[i]>a[j]):
            t=a[i]
            a[i]=a[j]
            a[j]=t
        elif(a[i]%2==1 and a[j]%2==1 and a[i]<a[j]):
            t=a[i]
            a[i]=a[j]
            a[j]=t
for i in a:
    print(i,end=' ')