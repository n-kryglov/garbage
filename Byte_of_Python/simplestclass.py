class Person:
    def __init__(self, name):
        self.name = name
    def sayHi(self):
        print ('Привет,', self.name)
p = Person ('Николай')
p.sayHi()