import re


s2= "ahdha31d5a8d"
tot=0
r= re.findall(r'[0,1,2,3,4,5,6,7,8,9]+',s2)
print r 
tot=0

for i in r:
    for j in range(1):
        print i[j].split()
        tot = tot + int(i)
print tot
    
    



'''s= "ahdheiuoiuiippp"
r = re.match("['a','e','i','o','u']+",s)
print r '''


