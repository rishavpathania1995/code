# Not so good sort , slow O(n)
# bogo sort
# random sort shuffle till get sorted list

#from __future__ import print_function
import random
#import doctest

def bogo(a, l):

    while (is_sorted(a, l) == False):
        shuffle(a, l)


def is_sorted(a, l):
    for i in range(l-1):
        if a[i] > a[i+1]:
            return False

    return True


def shuffle(a, l):

    for i in range(l-1):
        r = random.randint(0, l-1)
        a[i], a[r] = a[r], a[i]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    a = [5, 4, 3, 2,3]
    l = len(a)
    bogo(a, l)
    print("sorted list {}".format(a))

# it actually took 30-40 sec to sort this

