'''

# lamlda

sum = lambda x,y:x+y
product = lambda x,y:x*y

print(sum(3,4))
print(product(3,4))

#lambda : print("hello")

#map

num=[1,2,3,5,4,8]

list1=list(map(lambda x:x*2,num))
print(list1)

# filter

filter1 = list(filter(lambda x:x%2==0,num))
print(filter1)


#all when all elements are truthy
print(all(num))

#any when atleast a single is truthy
print(any([0,1,2,3]))

#generator expression

import sys
gen=(x*2 for x in range(100))
print(sys.getsizeof(gen))
print(gen)

# sorted

sorted(list,reverse=True)
sorted(list,key=len)

sorted(list ,key=lambda user :user['username'])
# max
#min

#reversed

[1,2,3].__len__()

#abs
#sum
#sum sum([1,2,3],10)    #16

# round(235.254)  #236
'''
#zip
num1=[1,2,3,4,5]
num2=[6,7,8,9,10]
z=zip(num1,num2)
print(list(z))



