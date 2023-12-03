n = input()
mp={}
if len(n)%2==1:
    n = n[:len(n)-1]
for i in range(0,len(n),2):
    x = int(n[i:i+2])
    if x in mp:
        mp[x]+=1
    else: mp[x]=1
for i in mp.keys():
    print(i,mp[i])