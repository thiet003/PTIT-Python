from math import log2
from math import pow
def toS(i):
    if i<=9: return str(i)
    return chr(ord('A') + i-10)
def convert(s):
    s=s[::-1]
    ans=0
    for i in range(len(s)):
        x=ord(s[i])-48
        ans+=(x*pow(2,i))
    return int(ans)

with open('DATA.in') as r:
# with open('D:\Work_2023\Lập trình Python\Codeptit\DATA.in') as r:
    for j in range(int(r.readline())):
        n = int(r.readline())
        x=int(log2(n))
        s = r.readline().strip()
        while len(s)%x!=0:
            s="0"+s
        ans=''
        while s!='':
            ans=toS(convert(s[-x:]))+ans
            s=s[:-x]
        print(ans)
