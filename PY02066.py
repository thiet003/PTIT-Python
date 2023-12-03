n = int(input())
a=[]
while True:
    try:
        a.extend([int(x) for x in input().split()])
    except:
        break
dem=0
for i in range(1,max(a)+1):
    if i not in a:
        dem+=1
        print(i)
if dem==0:
    print("Excellent!")