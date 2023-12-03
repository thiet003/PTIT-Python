def nenso(n):
    if len(n)==1:
        return 0
    sum=0
    for i in n:
        sum+=ord(i)-ord('0')
    return nenso(str(sum))+1
n = input()
if len(n)<=1:
    print(1)
else:
    print(nenso(n))