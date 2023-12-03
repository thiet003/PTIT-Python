n = int(input())
a=[]
for j in range(n):
    a.append(input())
while len(a)>0:
    id=len(a)
    for i in range(len(a)):
        if(a[i]==''):
            id=i
            break
    print(str(a[0])+": "+str(id-1))
    a=a[id+1:]