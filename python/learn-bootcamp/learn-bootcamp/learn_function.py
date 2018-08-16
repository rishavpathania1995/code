#learn function
'''
#flip coin function
from random import random
def flip_coin():
    if random()>0.5:
        print("heads")
    else:
        print("tails")

print(flip_coin())

# global
# nonlocal




# args
total=0
def sum(*args):   create a tuple
    global total
    for x in args:
        total+=x

    return total

print(sum(1,2,3,5,132123))


# **kwargs  create a dictionary

def print_color(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}:{v}")


print_color(harry="blue" ,pooter="red",rohit="black")


## parmeters odering

1 parameters
2 *args
3 default parameter
4 **kwargs


def test(a,b,*args,name="harry",**kwargs):
    print([a,b,args,name,kwargs])

test(1,2,3,name="rohit",classa="first")


#unpack tuple by passing (*num)
#unpach dict by passing (**num)

num=(1,3,2,1,3,3,2,2,3,2)
data=dict(name="rohit",color="red")
def sum(*args):
    total = 0
    for x in args:
        total+ = x
    return total

print(sum(*num))


def print1(name,color):
    print(f" {name}{color}")

print1(**data)

'''
