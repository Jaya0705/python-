from os.path import join


class File(object):

    def __new__(cls):
        print cls
        return super(File,cls).__new__(cls)

    def __del__(self):
        self.file.close()
        del self.file
        print ('finally')

    def __init__(self, filename='sample.txt'):
        self.file = open(join(filename), 'r+')
        print 'done'

class A(object):
    def __new__(cls, a, b, c):
        print "Creating Instance"
        instance = super(A, cls).__new__(cls)
        instance.__init__(a,b,c)
        return 3

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        print a+b*c

    def bar(self):
        pass


A(5, 6, 2)
File()