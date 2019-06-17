import unittest
a="i love python"
str=""
for i in a:
    str=i + str
print str


class test(unittest.TestCase):
    def test(self):
        self.assertEquals(str,"uyghytvtyhj")



if __name__ == '__main__':
    unittest.main()



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
