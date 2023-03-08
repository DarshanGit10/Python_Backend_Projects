# tables.py contains 
# 1. Create database(document) 
# 2. Create Collection(tables)
# 3. Inserting data into collection


import pymongo

# In connection String paste mongo connectivity link [local or cluster]
connectionString = ""

if __name__ == '__main__':
    client = pymongo.MongoClient(connectionString)
    # Create a DataBase
    db = client['student_DB']
    # Create a collection
    collection = db['student_Table']
    # Insert the data into collection
    studentInfo = [
        {"name": "John Smith", "age": 22, "major": "Computer Science", "GPA": 3.5},
        {"name": "Jane Doe", "age": 21, "major": "Biology", "GPA": 3.8},
        {"name": "Tom Jones", "age": 23, "major": "Mathematics", "GPA": 3.2},
        {"name": "Sarah Lee", "age": 20, "major": "History", "GPA": 3.9},
        {"name": "Mike Brown", "age": 22, "major": "Psychology", "GPA": 3.6},
        {"name": "Emily Chen", "age": 21, "major": "Chemistry", "GPA": 3.4},
        {"name": "Chris Lee", "age": 24, "major": "Physics", "GPA": 3.1},
        {"name": "Samantha Smith", "age": 20, "major": "English", "GPA": 3.7},
        {"name": "David Kim", "age": 22, "major": "Economics", "GPA": 3.3},
        {"name": "Kelly Davis", "age": 21, "major": "Political Science", "GPA": 3.5}
    ]
    x = collection.insert_many(studentInfo)
    print("Successfully inserted:", len(x.inserted_ids), "documents")
