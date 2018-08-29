'''
f = open("abc.txt",'r')
print(f.read())
f.seek(0)


file.readlines()    # create list
file.close()
file.closed # gives true or false


with open("abc.txt") as file:
    file.read()

print(file.closed)  # false

