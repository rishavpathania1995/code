# bubble sort

def bubble_sort(a, l):
    for i in range(l-1):
        swap = False
        for j in range(l-1-i):

            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swap = True
        if not swap:
            break
    return True


if __name__ == '__main__':

    a = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    bubble_sort(a, len(a))
    print(a)
