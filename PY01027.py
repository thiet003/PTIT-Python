n = input()
ok=True
i=0
while i < len(n):
    if i<=len(n)-3 and n[i:i+3]=="688":
        i+=3
        ok=True
    elif i<=len(n)-2 and n[i:i+2]=="68":
        ok=True
        i+=2
    elif str(n[i])=="6":
        ok=True
        i+=1
    else:
        ok = False
        break
if ok:
    print("YES")
else:
    print("NO")