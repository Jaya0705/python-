'''#converting list of tuples to list
a = [(1,), (2, 3), (4, 5, 6)]3.
l = [element for tup in a for element in tup]
print l

l=list(map(lambda i:i[0],a))
print l





#converting list to dict
l=[('a',0),('b',2),('c',3),('d',4),('e',5)]
d={key:value for key,value in l}
print d

print dict(l)'''




#converting list to dict if no values or keys given
a = ['a',2,3,4]
d = dict.fromkeys(a, 0)
print d

d = dict([(x,0) for x in a])
print d





'''#intersection of two lists
l1=[1,2,3,4,5]
l2=[2,3,4,5,6]
l3=[]
l4=[]
for a in l1:
    for b in l2:
        if a==b:
            pass
        else:
           l3.append(a)
s3=set(l3)
print s3'''


'''

def intersection(l1, l2): 
    l3 = [value for value in l1 if value in l2] 
    return l3 

l1 = [4,9,1,17,11,77,26,28,54,69] 
l2 = [9,9,74,21,45,11,7,63,28,26] 
print(intersection(l1, l2)) '''







