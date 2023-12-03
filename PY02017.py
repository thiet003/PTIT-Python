t = int(input())
for j in range(t):
    n = int(input())
    a=[int(x) for x in input().split()]
    mp={}
    for i in a:
        if i in mp:
            mp[i]+=1
        else:
            mp[i]=1
    for i in mp.keys():
        if mp[i]%2==1:
            print(i)
            break