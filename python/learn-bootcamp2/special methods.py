# special methods
'''
__add__
__repr__
__len__
__mul__

'''


class Human:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def __repr__(self):
        return f"{self.firstname}{self.lastname} {self.age}"

    def __len__(self):
        return self.age

    def __add__(self, other):
        if isinstance(other, Human):
            return Human(firstname="newborn", lastname=self.lastname,age=0)

    def __mul__(self, other):
        pass


h = Human("harry", "potter", 35)
h2 = Human("rohit", "sharma", 54)
print(len(h))
print(isinstance(h2, Human))
print(h + h2)



