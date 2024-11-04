#PRACTILE 5
#Define a function to count to take input of name, age, salary,
#designation and add it to a binary file named as record.dat.
#Create a function to fetch all records having age greater than 35.
import pickle
def add_record():
    f=open("record.dat", "wb")
    name = input("Enter name: ")
    age = float(input("Enter age: "))
    salary = float(input("Enter salary: "))
    designation = input("Enter designation: ")
    data=[name, age, salary,designation]
    pickle.dump(data,f)
    f.close()
add_record()

def fetch():
    f=open("record.dat", "rb")
    data=pickle.load(f)
    if data[1] > 35:
       print(data[0], data[1], data[2], data[3])
    f.close()
fetch()

