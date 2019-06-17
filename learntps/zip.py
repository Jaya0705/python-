"""for i in zip([1,2,3],['a','b','c'],['#','*','$']):
        print(i)"""


z=zip([1,2,3],['a','b','c'],['#','*','$'])
a,b,c=zip(*z)
print(a)
print(b)

