def fibo(n):
    if n in (0,1):
        return n
    else:
        return fibo(n-1)+fibo(n-2)
for i in range(0,10):
    print fibo(i)



a=0
b=1
print a 
for i in range (1,10):
    a,b=b,a+b
    print a


    
n= input("enter a value upto till fibo should generate")
first= 0
second = 1
print first
for i in range (n):
    temp = first
    first = second
    second = temp + first
    print first
