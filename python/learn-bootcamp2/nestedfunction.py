#nested function


def a():
    def b():
        print("in b")
    return b()
a()


def num(n,func):
    total =0
    for n in range(num):
        total += func(n)
    return total

def square(x):
    return x*x

print(num(5,square))



