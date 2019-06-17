from collections import Counter

s="helllllolpl"
s1=list(s)
print s1
c=Counter(s1)
print c

nd={}
e=[]
o=[]
for i in range(len(s)):
  if i%2==0:
    e.append(s[i])
  else:
    o.append(s[i])
print e,o


de=dict(Counter(e))
print de
dekeys=de.keys()
deval=de.values()




do=dict(Counter(o))
print do
dokeys=do.keys()
doval=do.values()



set1=set(dekeys).union(dokeys)
print set1
nl=list(set1)
print nl

for i in nl:
  if i in do.keys() and i in de.keys():
    nd[i]=abs(de[i]-do[i])
print nd

li_dif = [i for i in e + o if i not in e or i not in o] 
print li_dif

for k,v in nd.iteritems():
  if v>0:
    for i in range(v):
      li_dif.append(k)

# li_dif.extend(nd.keys())
print li_dif




