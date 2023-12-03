
with open('CONTACT.in','r') as file:
    se=set()
    s = file.readline()
    while s:
        s=s.strip()
        se.add(s.lower())
        s = file.readline().lower()
    se = sorted(list(se))
    for x in se:
        print(x)