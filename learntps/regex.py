import re
xx = "guru99 education,is fun"
r1 = re.findall(r"^\w+", xx)
print r1
print((re.split(r'\s','we are splitting the words')))
print((re.split(r's','split the words')))
