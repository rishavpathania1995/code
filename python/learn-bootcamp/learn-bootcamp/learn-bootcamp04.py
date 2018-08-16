# Range

'''
for x in range(1,10):
    print(x**2)

for letter in "coffe":
        print(letter)


# range (7)   starts form 0 to 7
# range(1,8)  starts for 1 to 7
# range (1,10,2)  prints 1 ,3 ,5
# range (7,0,-1 ) print 6 ,5 ,4,3,2,1
# r = range (1,8)
# list(r)


times = input("enter the no of times you want to enter ")
times = int(times)

for times in range (times):
    print(f"time :{times} please do you job ")




for number in range (1,21):
    if number == 4 or number==13:
        state = "unlucky number"

    elif number%2 == 0 :
        state = "Even No"

    else:
        state = "Odd no"

    print(f"Number: {number} is {state}")


#print unicode string

for x in range(1,10):
    string= ""
    count=x
    while count>0:
        string+= "\U0001f604"
        count-=1
    print(string*2)


#print tree
for x in range(1,10):
    i=x
    j=x
    while i<10 :
        print(" ",end="")
        i+=1
    while j :
        print("*",end="")
        j-=1
    print("")

'''


