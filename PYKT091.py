mp={}
# with open('D:\Work_2023\Lập trình Python\Codeptit\VANBAN.in','r') as file:
with open('VANBAN.in','r') as file:
    s = file.readline()
    while s:
        ds = s.split()
        for i in ds:
            if i==i[::-1]:
                if i in mp:
                    mp[i]+=1
                else:
                    mp[i]=1
        s=file.readline()
ans=0
for i in mp.keys():
    if len(i)>ans:
        ans=len(i)
for i in mp.keys():
    if len(i)==ans:
        print(i,mp[i])