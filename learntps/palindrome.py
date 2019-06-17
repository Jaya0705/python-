
a='madam'
b=''
c=len(a)-1
while c>=0:
  b= b + a[c]
  c=c-1 
print (b)

if a==b:
    print "palindrome"
else:
    print "not a palindrome"



s1 = "madam"
s2 = s1[::-1]
if s1 == s2:
    print "palindrome"
else:
    print "not a palindrome"
