import re
e=[]
def check(s):
    if(s[-1:]=="?" or s[-1:]=="." or s[-1:]=="?"):
        return True
    return False
while True:
    try:
        s = input()
        ds =s.split()
        ans=""
        
    except:
        break