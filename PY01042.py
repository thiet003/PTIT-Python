t = int(input())
for i in range(t):
    s=input()
    ok=0
    for j in s:
        if(j!='0' and j!='1' and j!='2'):
            ok=1
            break
    if(ok):
        print("NO")
    else:
        print("YES")