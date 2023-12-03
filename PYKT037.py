t = int(input())
for i in range(t):
    n,b = [int(x) for x in input().split()]
    s="";
    while n>0:
        x=n%b;
        if(x<=9):
            s=str(x)+s
        else:
            y = 65+x-10
            s=str(chr(y))+s
        n//=b;
    print(s)