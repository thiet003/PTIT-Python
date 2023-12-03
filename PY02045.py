def process(n):
    m=len(n)
    x = int(n[0:m//2])
    y = int(n[m//2:])
    print(x+y)
    if x+y <9:
        return
    else:
        process(str(x+y))
n = input()
process(n)
