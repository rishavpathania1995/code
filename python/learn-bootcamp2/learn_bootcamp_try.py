"""
# raise
#Typeerror
#Valueerror
# zerodivision error

def display(name,colors):
    color=["red","blue","green"]
    if type(name) is not str:
        raise TypeError("Name is not string")
    print(f"{name}{colors}")

display(1,"hello")


# finally
# else
try:
    var=int(input("enter a integer"))

except:
    print("Not integer")

else:
    print("in else")

finally:
    print("in finally")

"""
#pdb
#import pdb ;
# pdb.set_trace()
#l
#p
#c
#n next line




