n = int(input())
for j in range(n):
    s = input()
    dem=1
    a=[]
    b=[]
    c={}
    for i in range(len(s)):
        if s[i]=='(':
            a.append(s[i]+str(dem))
            b.append(dem)
            dem+=1
        elif s[i]==')':
            x = a[len(a)-1]
            h=x[:1]
            f=int(x[1:])
            if(h=="("):
                a.pop()
                b.append(f)
    for i in b:
        print(i,end=" ")
    print()
    
