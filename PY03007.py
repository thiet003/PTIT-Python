import re
x=""
while True:
    try:
        s = input()
        x+=s;
        # ds = re.split(r'[ \.\?\!]',s.lower())
        # print(ds)
    except:
        break
ds = re.split(r'[\.\?\!]',x.lower())
for i in ds:
    if i:
        res = i.split()
        ans=res[0][:1].upper()+res[0][1:]
        for j in range(1,len(res)):
            ans+=" "
            ans+=res[j]
        print(ans)        