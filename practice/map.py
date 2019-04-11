def multiply(x):
    return x*x
def add(x):
    return x+x

funcs = [multiply, add]
for i in range(5):
    print(list(map(lambda x: x(i), funcs)))
    



'''#diffbetweenfilter,reduce and map
def m(x): return x % 2 == 0
def f(y): return y * 2
def r(x,y): return x+y
list = [1,2,3,4]

flist = filter(f, list)
print(flist)

mlist = map(m, list)
print(mlist)

print(reduce(r,list))'''
