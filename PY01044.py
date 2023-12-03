s1 = [str(x) for x in input().split()]
s2 = [str(x) for x in input().split()]
# Giao
s={"d"}
s.remove("d")
for x in s1:
    s.add(x.lower())
ss={"a"}
ss.remove("a")
for x in s2:
    ss.add(x.lower())
sss = sorted(ss.intersection(s))
ssss = sorted(ss.union(s))
for x in ssss:
    print(x,end=' ')
print()
for x in sss:
    print(x,end=' ')