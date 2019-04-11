#togetkeys from values:
'''d={1:'k',2:'a',3:'h'}
li=[]
for key,value in d.iter():
    if(value=='h'):
        li.append(key)
print li


d ={'g':16,'a':19,'c':19}
inputvalue=input('enter value')
li=[key for key,value in d.items() if value==inputvalue]
print li'''




#converting list into dict:
'''t=[("a", 10),("g", 12),("j",14),("s",20),("k",25),("h",30)]
di={}
for a,b in t: 
        di.setdefault(a,[]).append(b) 
print di 
'''



l = ['a','b','c','d','e','']
d = dict([(k, v) for k,v in zip (l)])
print d



#difference b/w list comp n for loops:
'''li=[2,3,4,5,6]
l=[a for a in li if a%2!=0]
print l


l1=[]
for a in li:
   if a%2!=0:
        l1.append(a)
print l1


li=[]
for i in range(20):
   li.append(i*2)
print li


li=[i*2 for i in range(20) if i%2!=0]
print li
'''



#lambdafunction:
'''x=lambda a,b:a*b
print(x(4,5))

y=lambda a:a**2
print(y(4))'''



#use of anonymous functions with lambda:
'''li = [1,2,3,4,5,6,7,8,9,10] 
l2= list(filter(lambda x:(x%2 != 0),li)) 
print(l2) 

l3=list(map(lambda x:x*2,li))
print l3


from functools import reduce
li = [1,5, 10, 20, 50, 100] 
sum = reduce((lambda x,y: x+y), li) 
print (sum)
'''


#more examples on lambda with anonymous functions:
'''arr1 = [1, 3, 4, 5, 7] 
arr2 = [2, 3, 5, 6] 
r= list(filter(lambda x: x in arr1,arr2))  
print r


result = list(map(lambda x: 2**x, range(10)))
print result

seq=[1,2,3,4,5]
result = filter(lambda x: x%2 == 0, seq) 
print(list(result))



r= list(map(lambda x: x if (x!='e' and x!='r') else 'e' if x=='r' else 'r','grrksfoegrrks'))
print (''.join(r))
'''


#converting list to str
'''L = ['L','O','L']
print ''.join(L)

x = [1,2,3]
y = "'"+ ','.join(map(str, x))  + "'"
print y'''


'''#fibonacci using lambda
from functools import reduce
fib = lambda n: reduce(lambda x,_: x+[x[-1]+x[-2]],range(n-2),[0, 1]) 
print(fib(7))'''


#squareroot
'''n=int(input("ENTER AN INTEGER"))
for i in range(1,6):
 root=n**(1/float(i))
 if(int(root)**i==n):
      pwr=i
      print root
      print pwr'''
    
   

#function
'''def func1():
        Print 'jaya'  
print 'hi'
func1()'''









