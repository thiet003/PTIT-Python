n = int(input())
a=[]
for i in range(n):
    b=input()
    a.append(b)
sum=0
for i in range(n):
    dem2=0
    for j in range(n):
        if(str(a[i][j])=="C"):
            dem2+=1
        if(j==n-1 and dem2>1):
            sum+=(dem2*(dem2-1))//2
for i in range(n):
    dem2=0
    for j in range(n):
        if(a[j][i]=='C'):
            dem2+=1
        if(j==n-1 and dem2>1):
            sum+=(dem2*(dem2-1))//2
print(sum)
    
    