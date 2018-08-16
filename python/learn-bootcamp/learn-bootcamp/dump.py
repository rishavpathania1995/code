'''#n=int(input())

#list =[[[input(),input()]for x in range(1) ]for y in range(n)]
#print(list.sort(reversed()))

n=2
list1[n][2]=[]


for x in range(n):
    a=input()
    b=int(input())
    test=[a,b]
    list1.append(test)

if __name__ == '__main__':
    N = int(input())
    result = []
    for n in range(N):
        x = input().split(" ")
        command = x[0]
        if command == 'append':
            result.append(int(x[1]))
        if command == 'print':
            print(result)
        if command == 'insert':
            result.insert(int(x[1]), int(x[2]))
        if command == 'reverse':
            result == result.reverse()
        if command == 'pop':
            result.pop()
        if command == 'sort':
            result == result.sort()
        if command == 'remove':
            result.remove(int(x[1]))




n=int(input())
list =[[[input(),input()]for x in range(1) ]for y in range(n)]

for i in range(n):
    min_list=list[0][1]

'''

def print_formatted(number):
    # your code goes here
    for i in range(number+1):
        print("{}{}{}{}".format(i,oct(i),hex(i).upper(),bin(i)))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)