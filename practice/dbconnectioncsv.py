import csv
import mysql.connector 
        
db = mysql.connector.connect(host="localhost",user="root",password="root",db="proj2") 
cursor = db.cursor()

with open('C:\Users\jaya.lakshmi.selvam\Documents\proj2\empdata.csv', 'r') as f:
        csv_data = csv.reader(f)
temp=[list(i) for i in csv_data]
for row in range(1,len(temp)):
        #print(row)
        cursor.execute('INSERT INTO employee(eid,fname,lname,gender,emailid,dob,phone,doj,experience)''VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)',row)
        cursor.execute('INSERT INTO project(pid,pname)''VALUES(%s,%s)',row)
        cursor.execute('INSERT INTO supervisor(sid,sname)''VALUES(%s,%s)',row)
        cursor.execute('INSERT INTO Employee_Project(Employee_Id,Project_Id,Supervisor_Id,Rollon_date,Rolloff_date,Career_level,Work_location,Designation,Fiscal_year)VALUES("{}","{}","{}",{},{},{},"{}","{}","{}")'.format(temp[row][16],temp[row][17],temp[row][18],temp[row][19],temp[row][20],temp[row][21],temp[row][22],temp[row][23],temp[row][24])
    db.commit()        
    
cursor.close()
print ("Done")
