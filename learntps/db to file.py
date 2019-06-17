import mysql.connector 
import unicodedata
import os 

db = mysql.connector.connect(host="localhost", user="root", password="root", db="dbtofile", port="3306")
cursor = db.cursor()
cursor.execute("select * from names;")
res = cursor.fetchall()
print res
db.close()


li = []
for i in res:
    print i 
    j = i[0].encode()
    li.append(j)
print li


os.chdir('C:\\Users\\jaya.lakshmi.selvam\\Documents\\python')
for i in li:
    filename = i + '.txt'
    f = open(filename, 'w')
    f.close()
