li = ['Bournville','icecream']
y = 'nestle'
l = map(lambda x: y + x.split(',')[0][7:], li)
print l

l2 = map(lambda x: str.replace(x, "i", y), li)
print l2

