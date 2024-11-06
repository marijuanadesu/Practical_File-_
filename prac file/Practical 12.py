#PRACTICAL 12
'''Create a CSV file by entering user-id and password,
read and search the password for given userid.'''
import csv

def create_csv_file():
    with open('users.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["user_id", "password"])
        while True:
            user_id = input("Enter user ID: ")
            password = input("Enter password: ")
            writer.writerow([user_id, password])
            another = input("Do you want to add another user?(yes/no): ").lower()
            if another != 'yes':
                break

create_csv_file()

import csv

def search_password(user_id):
    with open('users.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == user_id:
                print(f"Password for user ID '{user_id}' is: {row[1]}")
                return
        print(f"No password found for user ID '{user_id}'")

user_id_to_search = input("Enter user ID to search: ")
search_password(user_id_to_search)
