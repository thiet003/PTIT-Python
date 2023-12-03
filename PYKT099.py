mp1={}
mp2={}
with open('DATA1.in','r') as file1:
    s=file1.readline()
    while s:
        ds = s.strip().lower().split()
        for i in ds:
            mp1[i]=1
        s=file1.readline()   
with open('DATA2.in','r') as file2:
    s=file2.readline()
    while s:
        ds = s.strip().lower().split()
        for i in ds:
            mp2[i]=1
        s=file2.readline()   
mp1 = dict(sorted(mp1.items(),key=lambda x: x[0]))
mp2 = dict(sorted(mp2.items(),key=lambda x: x[0]))
for i in mp1.keys():
    if i not in mp2:
        print(i,end=" ")
print()
for i in mp2.keys():
    if i not in mp1:
        print(i,end=" ")

