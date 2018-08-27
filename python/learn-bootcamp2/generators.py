# Generators
def gen(max):
    count = 1
    while count < max:
        yield count
        count +=1
g = gen(5)
print(next(g))
print(next(g))


# fibanachi number

def fib_gen(max):
    x = 0
    y = 1
    count = 0
    while count < max:
        x,y = y , x+y
        yield x
        count += 1

for n in fib_gen(100):
    print(n,end="")

print(sum([num for num in range[100]]))        # creating list then sum

print(sum(num for num in range[100]))   # generator expression

