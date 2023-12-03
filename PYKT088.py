import math
def soluonguoc(n):
    dem=0
    for i in range(1,int(math.sqrt(n))+1):
        if(n%i==0):
            dem+=1
            if(i!=n//i):
                dem+=1
    return dem
for i in range(1,1000000001):
    if(soluonguoc(i)==9):
        print(i,end=' ')