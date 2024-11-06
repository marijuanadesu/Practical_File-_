#PRACTICAL 9
'''Create a binary file with roll number, name and marks.
Input a roll number and update the marks.'''
import pickle
def add_record():
    f=open("students.dat", 'wb')
    name = input("Enter name: ")
    roll = int(input("Enter roll number: "))
    marks = float(input("Enter marks: "))
    data=[name,roll,marks]
    pickle.dump(data, f)
add_record()
def update_marks(roll_number, new_marks):
    records = []
    updated = False

    # Read all records from the file
    with open('students.dat', 'rb') as f:
        while True:
            try:
                record = pickle.load(f)
                records.append(record)
            except EOFError:
                break
    
    # Update the specified record
    with open('students.dat', 'wb') as f:
        for record in records:
            if record[1] == roll_number:
                record[2] = new_marks
                updated = True
            pickle.dump(record, f)

    if updated:
        print(f"Marks updated for roll number {roll_number}.")
    else:
        print(f"No record found for roll number {roll_number}.")

# Add a record
add_record()

# Input roll number and new marks
roll_number_to_update = int(input("Enter roll number to update: "))
new_marks = float(input("Enter new marks: "))

# Update the marks
update_marks(roll_number_to_update, new_marks)
