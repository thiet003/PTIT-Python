n = input()
k = int(input())
mp={}
if len(n)%2==1:
    n = n[:len(n)-1]
for i in range(0,len(n),2):
    x = int(n[i:i+2])
    if x in mp:
        mp[x]+=1
    else: mp[x]=1
mp = dict(sorted(mp.items(),key=lambda x: x[0]))
ok=1
for i in mp.keys():
    if mp[i]>=k:
        print(i,mp[i])
        ok=0

if ok==1:
    print("NOT FOUND")
    