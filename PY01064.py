t = int(input())
for i in range(t):
    n,k=map(int,input().split())
    dem=0
    while k%2==0:
        dem+=1
        k//=2
    print(chr(dem+ord('A')))