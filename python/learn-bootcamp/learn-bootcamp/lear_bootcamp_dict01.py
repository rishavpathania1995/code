'''
# creating dictionary
dict1={"name":"value",
       "class":"value",
       "rollno":"value"}

print(dict1)
dict2 = dict(name="harry", class1="1st")
print(dict2)


print(dict1["name"])
print(dict2["name"])



d1={"name":"harry potter",
       "class":"1st",
       "rollno":119}

for key in d1.keys():
       print(key)


for value in d1.values():
       print(value)


for k,v in d1.items():
       print()

if "name" in d1.keys():
       print("name")


if "harry potter" in d1.values():
       print("harry potter ")

if "name","harry potter" in d1.items():
       print("yes")
       
       



donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)

total_donations = 0

for donation in donations.values():

       total_donations += donation
print(total_donations)



# dictionary
#clear

d2={"name":"rohit",
    "class":"1st",
    "rollno":43}



#copy
#{}.fromkeys
#get

d3=d2.copy()
d2.clear()
print(d2)
print(d3)
print(d3.get('name'))


from random import choice
food= choice(["apple","orange","banana","grapes"])

item={
       "apples":5,
       "banana":6,
       "grapes":10

}

if food in item.keys():
       print("yes")
       print(food)

else:
       print("no")


if item.get(food):
    print(item.get(food))

else:
    print("value no present")



# pop
item={
       "apples":5,
       "banana":6,
       "grapes":10
}
item.pop("apples")
print(item)
# popitem
item.popitem()
print(item)
#update
item2={"grapes":1,
        "mangoes":2}

item2.update(item)
print(item2)



# dictionary comprehension

#even odd
dict1={num: ("Even" if num%2==0 else 'Odd') for num in range(1,100)}
print(dict1)
#upper case
dict2=dict(abc="dasd",ads="adas",ada="adad",a5a="asda")
print(dict2)
dict3={k.upper():v.upper() for k,v in dict2.items()}
print(dict3)

# list to Dictonary using dict compreension

str1=["name","class","rollno"]
str2=["harry potter","5th","23"]

dict4={str1[i]:str2[i] for i in range(len(str1))}

print(dict4)

'''

