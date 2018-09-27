# selection sort
# find th position of minimum value swap after that. Search than sort .

def selection_sort(a):

    for i in range(0, len(a)):
        imin = i
        for j in range(i+1,len(a)):
            if a[j] < a[imin]:
                imin = j

        if i != imin:
            a[i], a[imin] = a[imin], a[i]

if __name__ == '__main__':
    a = [5, 3, 3, 2, 1]
    selection_sort(a)
    print(a)


