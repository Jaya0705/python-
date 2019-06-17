class MyClass:
    x=0
    def method(self):
        print 'instance method called', self
        y=1
        print self.x
        print y

    @classmethod
    def classmethod(cls):
        print 'class method called', cls

    @staticmethod
    def staticmethod():
        print 'static method called'
        x,y=1000,1
        print x ,' ',y

o= MyClass()
o.staticmethod()
o.classmethod()
o.method()