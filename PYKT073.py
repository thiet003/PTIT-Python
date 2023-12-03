n = int(input())
ans=0
demlb=0
demtn=0
a=[]
for i in range(n):
    s = input()
    ds = s.split()
    if len(ds)==6:
        demtn=0
        demlb += 1
        if demlb == 1:
            a.append(1)
    elif len(ds) == 7:
        if demtn==4:
            demtn=0
        demtn +=1
        demlb = 0
        if demtn == 4:
            a.append(2)
print(len(a))
for i in a:
    print(i)