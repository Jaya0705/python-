class SuperClass(object):
    superpowers = []

    def __init__(self, name):
        self.name = name

    def add_superpower(self, power):
        self.superpowers.append(power)

foo = SuperClass('foo')
bar = SuperClass('bar')
print foo.name
print bar.name
foo.add_superpower('fly')
print bar.superpowers
print foo.superpowers
