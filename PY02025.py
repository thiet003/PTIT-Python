n,m = [int(x) for x in input().split()]
a =[int(x) for x in input().split()]
b =[int(x) for x in input().split()]
mp1={}
mp2={}
for i in a:
    mp1[i]=1
for i in b:
    mp2[i]=1
for i in range(1,1001):
    if i in mp1 and i in mp2:
        print(i,end=" ")
print()
for i in range(1,1001):
    if i in mp1 and i not in mp2:
        print(i,end=" ")
print()
for i in range(1,1001):
    if i not in mp1 and i in mp2:
        print(i,end=" ")