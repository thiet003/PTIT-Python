n,m = map(int,input().split())
a = [int(x) for x in input().split()]
mp={}
for i in range(1,m+1):
    mp[i]=0
for i in a:
    mp[i]+=1
maxx1=-1e9
maxx2=-1e9
for i in range(m):
    if i not in mp:
        continue
    x=mp[i]
    if x > maxx1:
        maxx2=maxx1
        maxx1=x
    elif x>maxx2 and x!=maxx1:
        maxx2=x
if maxx2 == -1e9:
    print("NONE")
else:
    for i in range(m):
        if i not in mp:
            continue
        if mp[i]==maxx2:
            print(i)
            break