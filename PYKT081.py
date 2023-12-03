def is_number(s):
    try:
        x=int(s)
        return True
    except ValueError:
        return False
t = int(input())
for i in range(t):
    s = input()
    a = s.split('.')
    ok=0
    if(len(a)!=4):
        ok=1
    else:
        for i in a:
            if not (is_number(i)):
                ok=1
                break
            i=int(i)
            if i<0 or i>255:
                ok=1
                break
    if ok==1:
        print("NO")
    else:
        print("YES")
