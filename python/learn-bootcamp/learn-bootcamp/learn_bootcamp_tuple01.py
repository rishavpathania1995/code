tup1=(1,3,3,2,12,2)
print(tup1)
#count
print(tup1.count(6))
#index
print(tup1.index(12))

#sets
s={1,3,"d","s","e","f",1}
print(s)
#add
s.add("alpha")
print(s)
#remove
s.remove("alpha")
print(s)
#discard
s.discard("alpha")
#copy
s1=s.copy()
#clear
print(s.clear())
#union| intersection &
s3={1,2,3,4,5}
s4={6,7,8,9}
print(s3|s4)
print(s3 & s4)

#set comprehension

s={x**2 for x in range(1,100000000000000000000000000000000000000000000)}
print(s)



#setcomprehenion






