import sys
from bisect import bisect_left
a=[1,2,4,6,12,24,36,48,60,120,180,240,360,720,840,1260,
   1680,2520,5040,7560,10080,15120,20160,25200,27720,45360,50400,55440,83160,
   110880,166320,221760,277200,332640]
t = int(input())
i=0
for line in sys.stdin:
    n=int(line)
    x=a[bisect_left(a,n)]
    print(x)
    i+=1
    if(i==t):
        break
    

