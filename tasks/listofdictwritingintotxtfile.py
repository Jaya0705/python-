li=[{'Name': 'John Doe', 'Age': 26, 'ID': '1279abc'}]
for dic in li:
   print dic
   with open('listofdictintofile.txt','w') as f:
       for keys,values in dic.items():
           print keys,' ',values
           f.write('{}:{}''\t'.format(keys,values))


            
            
import xlwt 
from xlwt import Workbook 
wb = Workbook()  
sheet1 = wb.add_sheet('sheet1') 
li=[{'Name':'John Doe', 'Age':26, 'ID':'1279abc'}]
row=0
col=0
for dic in li:
   for keys in dic.keys():
       sheet1.write(row,col,keys)
       row=row+1
       #for values in dic.values():
           #sheet1.write(row,col+1,values)
wb.save('listofdictintofile.xls')
   
