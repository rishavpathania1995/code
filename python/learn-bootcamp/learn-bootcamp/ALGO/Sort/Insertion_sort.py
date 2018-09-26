# Insertion sort

def insertion_sort(a):
    for index in range(1, len(a)):
        i = index
        while 0 < i and a[i] < a[i-1]:
            a[i], a[i-1] = a[i-1], a[i]
            i -= 1

if __name__ == "__main__":
    a = [2, 4, 2, 3, 4, 7, 3, 2, 1]
    insertion_sort(a)
    print(a)
