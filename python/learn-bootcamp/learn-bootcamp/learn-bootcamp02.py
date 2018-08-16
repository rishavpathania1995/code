"""
# if else program 
name=input("enter your name ")

if name == "harry" :
    print("hello harry")

elif name == "rohit":
    print("hello rohit")

else:
    print("please enter name")


"""
"""
# and , or ,not logical operators
# is and ==
a=[1,2,3]
b=[1,2,3]
if a is b :
    print("true")
"""
"""
# bouncer code example

user=input("please enter the age")

if user == '':
    print("please enter the age")
    user=input("")

age=int(user)

if not(age >=18):
    print("you are not allowed in concert")

if ((age >=18 ) and (age<=23)):
    print("you can enter concert but cant drink beer")

if (age>=24):
    print("you can drink anything even piss")
"""
