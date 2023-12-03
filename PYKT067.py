import itertools
for j in range(int(input())):
    n = int(input())
    a=[int(x) for x in range(1,n+1)]
    b = itertools.permutations(a,n)
    c=[]
    for i in b:
        c.append(''.join(map(str,i)))
    print(len(c))
    for i in range(len(c)-1,-1,-1):
        print(c[i],end=" ")
    print()