n = int(input())
a=[]
for j in range(n):
    a.append(input())
i = 0
while len(a)>0:
    # i=len(a)
    for x in range(len(a)):
        if(a[x]==''):
            i=x
            break
    print(str(a[0])+": "+str(i-1))
    a=a[i+1:]
