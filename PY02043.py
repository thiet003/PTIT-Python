for t in range(int(input())):
    s = input()
    k = input()
    n=len(k)
    i = 0
    dem=0
    while i < len(s):
        if i<=len(s)-n and s[i:i+n]==k:
            dem+=1
            i+=n
        else: i+=1
    print(dem)
