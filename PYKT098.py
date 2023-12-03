with open('DATA.in','r') as file:
# with open('D:\\Work_2023\\Lập trình Python\\Codeptit\\DATA.in','r') as file:
    ds=[]
    for dong in file:
            x = dong.split();
            for i in x:
                try:
                    y = int(i)
                    if(y>1e18):
                         ds.append(i)
                except:
                    ds.append(i)
    ds = sorted(ds)
    for x in ds:
         print(x,end=" ")