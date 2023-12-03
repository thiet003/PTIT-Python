while True:
    n = int(input())
    if n==0: break
    a=[]
    for i in range(n):
        a.append(int(input()))
    ok=0
    for i in range(n-1):
        if(a[i]!=a[i+1]):
            ok=1
    if ok==1:
        print(min(a),max(a))
    else:
        print("BANG NHAU")