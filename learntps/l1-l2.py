
'''
s="helllllolpl"


nd={}
l1=[]
l2=[]
for i in range(len(s)):
  if i%2==0:
    l1.append(s[i])
  else:
    l2.append(s[i])
print l1,l2



nl=[]
a=0
l1_c=copy.deepcopy(l1)

'''
import copy 
l1=[1,2,3,4]
l2=[2,3,4,5]
l1c=copy.deepcopy(l1)

for i in l2:
    if i in l1:
        c1=l1.count(i)
        c2=l2.count(i)
        print c1,c2
        fc=abs(c1-c2)
        if i in l1c:
            for k in range(fc):
                nl.append(i)
        
            
            for l in range(c1):
                l1c.remove(i)
    else:
        nl.append(i)
#nl.extend(l1c)
print nl
