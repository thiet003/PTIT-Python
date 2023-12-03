def out(a):
    s=""
    s+='('
    s+=str(a[0])
    for i in range(1,len(a)):
        s+=" "
        s+=str(a[i])
    s+=')'
    return s
def process(a):
    m=len(a)
    i=len(a)-1
    while a[i]==1: 
        i-=1
        a.pop()
    if i<0:
        return 0
    a[i]-=1
    n=m-i
    p=n//a[i]
    q=n%a[i]
    for j in range(p):
        a.append(a[i])
    if q!=0: a.append(q)
    return a
for i in range(int(input())):
    n = int(input())
    a=[]
    e=[]
    a.append(n)
    dem=0
    while True:
        dem+=1
        e.append(out(a))
        if len(a)==n:
            break
        a=process(a)
    print(len(e))
    for i in e:
        print(i,end=" ")
    print()
        