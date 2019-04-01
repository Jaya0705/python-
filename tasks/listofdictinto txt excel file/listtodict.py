keys = []
values = []
di={}
c = int(input("Input total no. of elements in the lists:"))
ch=int(input('enter choice'))
if ch==1:
    for i in range(0, c):
        e=str(input("Input key" +str(i+1)+ ":"))
        keys.append(e)

    for i in range(0, c):
        e=int(input("Input value" +str(i+1)+ ":"))
        values.append(e)
    dic = dict(zip(keys,values))
else:
    for i in range(0, c):
        a=str(input("Input key" +str(i+1)+ ":"))
        keys.append(a)
        values.append(di.setdefault(None))
    dic=dict(zip(keys,values))
print(dic)



