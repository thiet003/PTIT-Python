e=[]
for i in range(int(input())):
    s=input()
    j=0
    d=0
    ok=0
    while j<len(s):
        d=0
        ok=0
        while j<len(s) and str(s[j]).isdigit():
            d=d*10+int(s[j])
            j+=1
            ok=1
        if ok==1:
            e.append(d)
        j+=1
e.sort()
for i in e:
    print(i)
