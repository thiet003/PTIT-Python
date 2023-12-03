for j in range(int(input())):
    ds=input().split()
    ans=len(ds[0])
    print(ds[0],end="")
    for i in range(1,len(ds)):
        ans+=(len(ds[i])+1)
        if ans >= 100:
            break
        print(" "+ds[i],end="")
    print()