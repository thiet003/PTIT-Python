n = int(input())
a=[int(x) for x in input().split()]
maxx=-1e9
a.sort()
maxx=max(maxx,a[n-1]*a[n-2])
maxx=max(maxx,a[n-1]*a[n-2]*a[n-3])
maxx=max(maxx,a[0]*a[1])
maxx=max(maxx,a[0]*a[1]*a[n-1])
print(maxx)