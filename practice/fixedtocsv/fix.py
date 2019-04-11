import csv
ff= open('rawdata.prn', 'r') 
cf= open('output.csv', 'w')
writer = csv.writer(cf)
line = ff.readlines()
print line
for row in line:
     writer.writerow(row.split())

ff.close()
cf.close()
