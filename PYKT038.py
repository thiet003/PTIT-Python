ds = {
    "000":0,
    "001":1,
    "010":2,
    "011":3,
    "100":4,
    "101":5,
    "110":6,
    "111":7,
}
n = input()
while len(n)%3!=0:
    n="0"+n;
for i in range(0,len(n),3):
    s=n[i:i+3];
    print(ds.get(s),end='')
