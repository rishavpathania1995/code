import csv
'''
with open("cars.csv") as file:
    read = csv.reader(file)
    lis = list(read)
    for x in lis:
        print(x)

with open("cars.csv") as file2:
    read2 = csv.DictReader(file2, delimiter=";")
    for y in read2:
        print(y)


with open("cats.csv","w") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["name", "age"])
    csv_writer.writerow(["rohit",12])
    csv_writer.writerow(["ankit",13])


with open("abc.csv","w") as file2:
    header =["name", "rollno"]
    csv_writer2 = csv.DictWriter(file2, header)
    csv_writer2.writeheader()
    csv_writer2.writerow({"name":"ankit","rollno":14})
    
'''

import pickle
with open("abc","wb") as file:
     pickle.dump(['as','asd'], file)

with open("abc","rb") as file2:
    pickle.load(file2)

