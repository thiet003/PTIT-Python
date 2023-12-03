t = int(input())
for j in range(t):
    s = input()
    sum=0
    x=""
    for i in s:
        if i.isdigit():
            sum+=int(i)
        else:
            x=x+i
    x=sorted(x)
    for i in x:
        print(i,end='')
    print(sum)