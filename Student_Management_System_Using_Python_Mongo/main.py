# main.py contains
# 1. A small user end program for user input
# 2. CRUD operations


import pymongo
import pandas as pd
from tabulate import tabulate


# In connection String paste mongo connectivity link [local or cluster]
connectionString = ""

def displayStudent():
    #Normal Way of printing
    # for doc in collection.find():
    #     print(doc)

    #Using Pandas
    # data = collection.find({}, {'_id': 0})
    # df = pd.DataFrame(list(data))
    # # specify index column and starting value
    # df.index += 1
    # # print table with index column
    # print(tabulate(df, headers='keys', tablefmt='psql', showindex=True))


    # Without using pandas
    data = collection.find({}, {'_id': 0})
    students = list(data)
    # format data into a list of lists
    table = [[i+1, student['name'], student['age'], student['major'], student['GPA']] for i, student in enumerate(students)]
    # print table with headers and index column
    headers = ['No.', 'Name', 'Age', 'Major', 'GPA']
    print(tabulate(table, headers=headers, tablefmt='psql', showindex=False))

def insertStudent():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    major = input("Enter your major: ")
    gpa = input("Enter your GPA: ")
    studentInfo = {"name": name, "age": age, "major": major, "GPA": gpa}
    collection.insert_one(studentInfo)
    print("Student data inserted successfully.")


def updateStudent():
    name = input("Enter student name to update: ")
    update_field = input("Enter field to update: ")
    update_value = input("Enter new value: ")
    result = collection.update_many({"name": name}, {"$set":{update_field:update_value}})
    if result.modified_count > 0:
        print(f"{result.modified_count} records deleted successfully.")
    else:
        print("Student not found.")

def deleteStudent():
    name = input("Enter student name to delete: ")
    result = collection.delete_many({"name": name})
    if result.deleted_count > 0:
        print(f"{result.deleted_count} records deleted successfully.")
    else:
        print("Student not found.")


if __name__ == '__main__':
    client = pymongo.MongoClient(connectionString)
    db = client['student_DB']
    collection = db['student_Table']
    while True:
        print("Select an operation:")
        print("1. Display data")
        print("2. Insert data")
        print("3. Update data")
        print("4. Delete data")
        print("5. Exit")
        userInput = int(input("Enter your choice: "))
        if userInput == 1:
            displayStudent()
        elif userInput == 2:
            insertStudent()
        elif userInput == 3:
            updateStudent()
        elif userInput == 4:
            deleteStudent()
        elif userInput == 5:
            print("Exiting the Program")
            break
        else:
            print("Invalid Input. Please enter a number between 1 and 5.")

    