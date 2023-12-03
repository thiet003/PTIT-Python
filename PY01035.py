n = input()
while len(n)%3!=0:
    n="0"+n
for i in range(0,len(n),3):
    x = n[i:i+3]
    if(x=="000"):
        print(0,end='')
    if(x=="001"):
        print(1,end='')
    if(x=="010"):
        print(2,end='')
    if(x=="011"):
        print(3,end='')
    if(x=="100"):
        print(4,end='')
    if(x=="101"):
        print(5,end='')
    if(x=="110"):
        print(6,end='')
    if(x=="111"):
        print(7,end='')