'''
class Animal:
    cool = True

    def sound(self, s):
        return f"i make sound {s}"


class Cat (Animal):
    Animal.__init__(self,name,species)   # calling attributes of parent class
    super().__init__(name,species)       # using super to call parent class

c = Cat()
print(c.sound("miau"))



class Human:
    def __init__ (self, firstname, lastname, age):
        self._firstname = firstname
        self._lastname = lastname
        self._age = age
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,age):
        if age>0:
            self._age=age
        else:
            self._age


n = Human("harry","potter",24)
print(n.age)
n.age=12
print(n.age)


#MRO   method resolution order

classname.mro()
classname__mro__
help(classname)

'''



