s = input()
s2 = input()
x = int(input())
x-=1
if(x==0):
    print(s2+s)
else:
    print(s[:x]+s2+s[x:])