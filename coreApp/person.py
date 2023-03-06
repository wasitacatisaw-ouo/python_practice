class Person:
    def __init__(self, name, age, addr):
        self.name=name
        self.age=age
        self.addr=addr
    def greeting(self):
        print('Hi, im {0} living in {1} and im {2} years old'.format(self.name, self.addr, self.age))        
    def eat(self, food):
        print('I ate %s!'%food)