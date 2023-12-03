t = int(input())
for j in range(t):
    s=""
    n,k = [int(x) for x in input().split()]
    while n >0:
        x = n%k
        if x<10:
            s=str(x)+s
        else:
            x-=10
            y=chr(65+x)
            s=str(y)+s
        n//=k
    print(s)