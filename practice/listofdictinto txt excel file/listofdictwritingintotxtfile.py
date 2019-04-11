'''li=[{'Name': 'John Doe', 'Age': 26, 'ID': '1279abc'}]
for dic in li:
   print dic
   with open('listofdictintofile.txt','w') as f:
       for keys,values in dic.items():
           print keys,' ',values
           f.write('{}:{}''\t'.format(keys,values))'''
         
     
      
import xlwt 
from xlwt import Workbook 
wb=Workbook()  
sheet1 = wb.add_sheet('Sheet1')    
li=[{'Name':'John','Age': 26,'ID':01},{'Name':'Jaya','Age':23,'ID':02}]

row=0
col=0
'''for col,key in enumerate(li[0].keys):
        sheet1.write(0,col,key)
        col=col+1'''
for key in li[0].keys():
        sheet1.write(0,col,key)
        col=col+1
row =1
col=0
for dic in li:
   for value in dic.values():
         sheet1.write(row,col,value)
         col=col+1
   col=0
   row=row+1
wb.save('listofdictintofile.xls') 
      
     



'''import xlwt 
from xlwt import Workbook  
wb = Workbook()
# add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('Sheet 1') 
  
sheet1.write(1, 0, 'ISBT ') 
sheet1.write(2, 0, 'SHAS') 
sheet1.write(3, 0, 'CLE') 
sheet1.write(4, 0, 'RA') 
sheet1.write(5, 0, 'CLOR') 
sheet1.write(0, 1, 'ISBT DEHRADUN') 
sheet1.write(0, 2, 'SHASTRADHARA') 
sheet1.write(0, 3, 'CLEMEN TOWN') 
sheet1.write(0, 4, 'RAJPUR ROAD') 
sheet1.write(0, 5, 'CLOCK TOWER') 
  
wb.save('sample xls.xls') '''





'''import csv
li=[{'Name':'John','Age': 26},{'Name':'Jaya','Age':23}]
with open('output.csv','wb') as output:
    writer = csv.writer(output)
    for dic in li:
        for keys,values in dic.items():
           print keys,' ',values
           output.write('{},{},'.format(keys,values))'''

