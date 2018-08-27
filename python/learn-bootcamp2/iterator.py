# iterator

'''
name = "harry potter"

it = iter(name)
while True:
    print(next(it))



def my_for(iterable,func):
    it = iter(iterable)
    i = next(it)
    while True:
        try:
            print(next(it))

        except StopIteration:
            print('end of file')
            break
        else:
            func(i)

def square(x):
    return x*x
my_for([1,2,3,1,2],square)

class Counter:
    def __init__(self, low, high):
        self.start = low
        self.stop = high
    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.stop:
            num = self.start
            self.start+=1
            return num

for x in Counter(1,10):
    print(x)

'''