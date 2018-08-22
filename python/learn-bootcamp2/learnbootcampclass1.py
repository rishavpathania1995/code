'''

class abc:
    def __init__ (self, name, rollno):
        self.name=name
        self.rollno=rollno

#user1=abc("harry", 25)
user2=abc("rohit", 26)
print(type(user1))
print(type(user2))
print(user1.name)
print(user2.rollno)

# A User class with 3 attributes but no methods (aside from __init__)
class User:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age

user1 = User("Joe","Smith", 68)
user2 = User("Blanca", "Lopez", 41)
print(user1.first, user1.last, user1.age)
print(user2.first, user2.last, user2.age)


_name
__name print(dir instance name) objectname._classname__name
__name__ dunders

'''

#class attribute
#class method


class User:

    totaluser=0  #class atribute

    @classmethod
    def total_user(cls):
        return f"{cls.totaluser}"

    @classmethod
    def decode_str(cls,data):
        name1,last1,age=data.split(",")
        return cls(name1,last1,age)


    def __init__(self,name,lastname,age):
        self.name=name
        self.lastname=lastname
        self.age=age
        User.totaluser+=1

    def fullname(self):
        return f"{self.name}{self.lastname}"

    def chksenior(self):
        if(self.age>60):
            return f"senior person"



user1=User("rohit","sharma",56)
user2=User("harry","potter",25)
print(user1.fullname())
print(user2.fullname())
print(user1.chksenior())
print(user2.chksenior())

print(User.totaluser)
print(User.total_user())



