def ktr(s):
    if s[len(s)-3]!='.':
        return False
    x=s[-2:]
    if x.lower()!='py':
        return False
    y = s[0:len(s)-3]
    for i in y:
        if(not ((i>='a' and i<='z') or (i>='A' and i<='Z') or i=='_' or i=='.')):
                return False
    return True
s = input()
if ktr(s):
    print("yes")
else:
    print("no")
