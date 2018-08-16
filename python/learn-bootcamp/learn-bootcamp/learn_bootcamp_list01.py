# list is also a function in class list

'''
r = list (range (1,5))

list1 = [1,"2","hello  world ", "my name is khan"]


len(list1 )



color = ['red', 'blue' , 'green']

if 'red' in color:
    print(color[0])
elif 'blue' in color:
    print (color[1])
elif 'green' in color:
    print(color[2])
else:
    print("no color")



# iteration over list for loop and while loop

colors = ['red' , 'blue' , 'green' , 'yellow']

for color in colors:
    print (color.upper())

i=0

while i < len(colors):
    print(f"index:{i} color is {colors[i].upper()}")
    i+=1

#adding in list
# append
# extend
# insert
list1=[1,2,3,4,5]
list1.append(6)
list1.extend([7,8,9])
list1.insert(0,0)
list1.insert(len(list1),10)
list2=[11,12,13,14,15]
list1.extend(list2)
print(list1)
print(len(list1))

list1.insert(20,20)
print(list1[20])



# clearing list
# clear  clear full list
# pop    clear at end of specified field
# remove  remove particular code

lis_car=["honda" , "bmw" , "maruti" , "fiat" , "hyundai"]

lis_car.pop()
print(lis_car)
lis_car.remove("fiat")
print(lis_car)
lis_car.pop(2)
print(lis_car)
lis_car.clear()
print(lis_car)



# index()   index("red",1,6)
# count("red")
# reverse()
# sort
# .join()


colors = ["red","blue","green","red","violet","red","blue","green"]
print(colors.index("red"))
print(colors.index("red",2,4))
print(colors.index("red",5))

print(colors.count("red"))
print(colors.sort())
colors.reverse()
print(colors)

print("this is color:".join(colors))




# slicing list

#list[start:stop:step]

colors= ["red","blue","orange","green","yellow","violet"]
print(colors[:])
print(colors[1:])
print(colors[1:5])
print(colors[-1:])
print(colors[-1:-5])
print(colors[1:5:1])
print(colors[-1:-5:-1])

#"helloworld"[0:2]  # "he"

string ="hello world"

print(string[::-1])

names =["harry","potter"]

names[0],names[1] = names[1],names[0]

print(names[0]+names[1])




#list comprehension

num =list(range(1,10))

num1=[i**2 for i in num]
print(num1)

num2=[str(i)for i in num]
print(num2)

num3 = [bool(i) for i in num]
print(num3)

num4 =[i*2 for i in num if i%2==0]
print(num4)  #  even print

num5=[i*2 if i%2==0 else i/2 for i in num]
print(num5)


# .join in comprehension
# 2d list
lis2d=[[1,2,3],[4,5,6],[7,8,9]]

for a in lis2d:
    for b in a:
        print(b)



# 2d list comprehension

lis2d1=[[b*2 if b%2 ==0 else b/2 for b in a]for a in lis2d]
print(lis2d1)
# print *** *** *** format

lis2d2 = [["X" if d%2==0 else "O" for d in range(1,4)]for c in range(1,4)]

print(lis2d2)



x = int ( input())
y = int ( input())
z= int(input())
n = int ( input())
ar = []
p = 0
for i in range ( x + 1 ) :
    for j in range( y + 1):
        if i+j != n:
            ar.append([])
            ar[p] = [ i , j ]
            p+=1
print(ar)

x = int ( input())
y = int ( input())
z= int(input())
n = int ( input())#lis2d3 = [[e,f] for f in range(y+1) for e in range (x+1) if (e+f)!=n]

#lis2d3=[[f if (f+e)!=n for f in range (y+1)]for e in range(x+1)]
lis2d4 = [[e,f,g]for g in range(z+1) for f in range(y+1) for e in range (x+1) if (e+f+g)!=n]
print(lis2d4)

lis2d5=[[[[e,f,g]  for e in range(x+1) if (e+f+g)!=n] for f in range(y+1)]for g in range[z+1]]


print(lis2d5)


'''



# reading data from file



file=open("nse-drop-copy.1.txt","r")



​



for f in file:



rishav [6:25 PM]

f=open("nse.txt","r")

#f2=open("trades_2018-08-09.csv","r")

lines=f.readlines()

#lines2=f2.readlines()

result=[]

result2=[]

result3=[]

for x in lines:

   result.append(x.split(',')[7])

f.close()

for y in result:

   result2.append(int(y.split(':')[1]))for z in range(len(result2)-1):

   result3.append(int(result2[z]))#print(result3)f2=open("trades_2018-08-09.csv","r")

lines2=f2.readlines()

result4=[]

result5=[]

result6=[]

for e in lines2:

   result4.append(e.split(",")[11])

f2.close()for f in range(len(result4)-1):

   result5.append((result4[f]).split('"'))for g in range(len(result4)-1):

   result6.append(int(result5[g][1]))#print(result3)

print(result3)

print(result6)

print(len(result3))

print(len(result6))print(len(set(result3)))

print(len(set(result6)))

#print(set(result3) & set(result6))

#print(len(result))

Message Input





Jot something down
