#PRACTICAL 8
''' Create a binary file with name and roll number.
 Search for given roll number and display,
 if not found display appropriate message.'''
import pickle

def add_record():
    f=open("students.dat", 'wb')
    name = input("Enter name: ")
    roll = int(input("Enter roll number: "))
    data=[name,roll]
    pickle.dump(data, f)
add_record()

def search_record():
    while True:
          f=open("students.dat", 'rb')
          data = pickle.load(f)
          if data[1]==search_roll_num:
             print(data[0], data[1])
          else:
              print("Roll number not found")
          f.close()
    
search_roll_num = int(input("Enter roll number to search: "))
search_record()

