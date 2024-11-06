#PRACTICAL 13
'''Define a function to take input of name, age, salary and city and 
add it csv file record.csv and also create a function to
 fetch all records having city as 'Delhi'.'''
import csv

def add_record():
    with open('record.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        salary = float(input("Enter salary: "))
        city = input("Enter city: ")
        writer.writerow([name, age, salary, city])

# Add a record
add_record()

def fetch_records_by_city(city_name):
    with open('record.csv', 'r') as file:
        reader = csv.reader(file)
        print(f"Records with city '{city_name}':")
        for row in reader:
            if row[3].lower() == city_name.lower():
                print(row)

# Fetch records with city 'Delhi'
fetch_records_by_city('Delhi')
