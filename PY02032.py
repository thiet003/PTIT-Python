n = input()
mp={1}
mp.remove(1)
if len(n)%2==1:
    n = n[:len(n)-1]
for i in range(0,len(n),2):
    mp.add(int(n[i:i+2]))
mp = sorted(mp)
for i in mp:
    print(i,end=" ")