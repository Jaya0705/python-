string = raw_input("Enter string:")

counts = {i:0 for i in 'aeiouAEIOU'}

for char in string:
    if char in counts:
        counts[char] += 1
for k,v in counts.items():
    print(k, v)






s= "a13chdjcj"
tot=0
for i in s:
    if i.isdigit():
        tot = tot+int(i)
print tot


l=['a','e','i','o','u']



