import mysql.connector as m

db = m.connect(host="localhost", user="root", password="root", db="mydb", port="3306")
cursor = db.cursor()
cursor.execute("select * from names;")
res = cursor.fetchall()
print res
db.close()

import unicodedata

li = []
for i in res:
    # this block will remove unicode character if it exists
    j = i[0].encode()
    li.append(j)
print li

import os

os.chdir('C:\\Python27\\programs\\files')
for i in li:
    filename = i + '.txt'
    f = open(filename, 'w')
    f.close()
