class myClass:
    name = 'Yan'

    def sayHi(self):
        # type: () -> object
        print 'Hello %s' % self.name


mc = myClass()
print mc.name
mc.sayHi()
