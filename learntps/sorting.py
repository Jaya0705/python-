a = ['a', 'b','z','x' ,'c']
print ord(a[0])
for i in range(len(a)-1):
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
           temp = a[i]
           a[i] = a[i+1]
           a[i+1] = temp
print a


 

n= raw_input("enter a no")
li=list(map(int,n.split(' ')))
print li
print(type(n))
