t = int(input())
for i in range(t):
    n = int(input())
    f = [0]*100001
    a = [int(x) for x in input().split()]
    st = []
    for j in range(n):
        while len(st)>0 and a[st[len(st)-1]]<=a[j]:
            st.pop()
        if len(st) == 0:
            f[j]=j+1
        else:
            f[j]=j-st[len(st)-1]
        st.append(j)
    for j in range(n):
        print(f[j],end=" ")
    print()