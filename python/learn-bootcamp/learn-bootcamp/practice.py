def ar(*args):
    for x in args:
        print(x)


if __name__ == "__main__":
    ar(1,2,3,4,5)


def kw(**kw):
    for key, value in kw.items():
        print("{}:{}".format(key, value))


if __name__ == "__main__":
    kw(name = "harry", classa = '7')




# generator funtion

def gen(n):
    for i in range(n):
        yield i

g = gen(5)
for x in range(5):
    print(next(g))
