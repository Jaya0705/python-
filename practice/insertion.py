import csv
import mysql.connector 
        
db = mysql.connector.connect(host="localhost",user="root",password="root",database="proj2",port="3306") 
cursor = db.cursor()

csv_data = csv.reader(file('C:\Users\jaya.lakshmi.selvam\Documents\proj2\empdata.csv'))

temp=[list(i) for i in csv_data]
for row in range(1,len(temp)):
    cursor.execute('INSERT INTO employee(eid,fname,lname) VALUES ("{}","{}","{}");'.format(temp[row][0],temp[row][1],temp[row][2]))
db.commit()
cursor.close()
print "Done"




