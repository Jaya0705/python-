l1=[1,2,3,4,5]
l2=[2,3,4,5,6,7]
#c=zip(l1,l2)
#print c

if len(l2) >= len(l1):
    target, iterate = [l1, l2]
else:
    target,iterate = [l2, l1] 



s = []
#for i,j in zip(iterate,target):this works only when two lists are of equal length 
for i in range(len(iterate)):
    for j in range(len(target)):
      element = iterate[i]
      element2 =target[j]
      
      if element not in target:
               s.append(element)
      elif element2 not in iterate:
               s.append(element2)
      
               
f=list(set(s))

print f
