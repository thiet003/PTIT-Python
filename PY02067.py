def check(a,i):
    for j in a:
        if j//i == j//(i+1):
            return False
    return True
n = int(input())
a = [int(x) for x in input().split()]
ans=0
for i in range(min(a),0,-1):
    if check(a,i):
        for j in range(n):
            ans+=(a[j]//(i+1)+1)
        break
print(ans)