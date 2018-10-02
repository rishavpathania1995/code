# shell sort

def shell_sort(a):
    # marcin curin gap sequence
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]

    for gap in gaps:
        i = gap

        while i < len(a):
            j = i
            temp = a[i]
            while j >= gap and a[j-gap] > temp:
                a[j] = a[j-gap]
                j -= gap

            a[j] = temp
            i +=1


if __name__ == "__main__":
    a = [1,2,6,4,5]
    shell_sort(a)
    print(a)