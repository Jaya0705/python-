n=input('enter a bin number')
temp = n
s=0
i=0
digit=0
while temp!=0:
   print temp
   digit = temp % 10
   s=s+digit*(2**i)
   temp = temp//10
   i=i+1
print s





s=raw_input('enter a string of num n char')
try:
   sum=0
   li=0
   #li=[x for x in s if i.isdigit()]
   for i in s:
      if i.isdigit():
         sum=sum+int(i)
      else:
         raise ValueError

  # for i in li:
     # sum=sum+int(i)
   print sum
   
except ValueError as e:
   print('character found')
      




import math
print eval('1 + 2 * 3')
print eval('math.sqrt(5)')
print eval('type(math.pi)')





def nsr():
  n=int(raw_input())
  a=n/float(2)
  print a
  b=(a+(n/a))/float(2)
  print b
  while a!=b:
      a=b
      b=(a+(n/a))/float(2)
  print b
nsr()


'''



l = []
l1 = []
def nsr():
    for n in range(1,10):
        a=n/float(2)
        b=(a+(n/a))/float(2)
        while a!=b:
            a=b
            b=(a+(n/a))/float(2)
        nsr=b

        l.append(nsr)
nsr()


def msr():
    for n in range(1,10):
        msr=pow(n,0.5)
        l1.append(msr)
    
msr()

print"----------------------------------------------------------"
print "Number|","N.Square Root|","\t","M.Square Root|","\t","Difference"
print"----------------------------------------------------------"
for i in range(min(len(test),len(test1))):
    
    print "   ",i+1,"|\t","%.11f|" %l[i],"\t","%.11f|" %l1[i],"\t",l[i]-l1[i]
print"----------------------------------------------------------"



   
