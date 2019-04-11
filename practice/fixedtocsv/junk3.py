import csv
ff= open('fixed len file.txt', 'r') 
cf= open('output.csv', 'w')
writer = csv.writer(cf)
line=ff.readlines()    
print line

li=[]
finalli=[]

for i in line:
    empid=i[0:3]
    empname=i[3:12]
    salary=i[12:20]
    
    eid=empid.strip()
    en=empname.strip()
    s=salary.strip()
    
    li.append(eid)
    li.append(en)
    li.append(s)
    
finalli.append(li)
print finalli
writer.writerows(finalli)

ff.close()
cf.close()


    
