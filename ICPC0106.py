import math
for j in range(int(input())):
    n = int(input())
    s=int(input(),2)
    ans=""
    while s >0:
        x=s%n
        if x<10:
            ans=str(x)+ans
        else:
            ans=chr(ord('A')-10+x)+ans
        s//=n
    print(ans)
    