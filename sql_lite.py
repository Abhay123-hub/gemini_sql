import sqlite3

# Connect to SQLite database (creates 'student.db' if it doesn't exist)
connection = sqlite3.connect("student1.db")

# Create a cursor object to insert records and create the table
cursor = connection.cursor()

# Create the table if it doesn't already exist
table_info = """
        CREATE TABLE IF NOT EXISTS STUDENTS3 (
        NAME VARCHAR(25),
        CLASS VARCHAR(25),
        SECTION VARCHAR(25)
        );
"""
cursor.execute(table_info)

# Insert some records into the table
cursor.execute('''INSERT INTO STUDENTS3 VALUES("Adam", "Data Science", "A")''')
cursor.execute('''INSERT INTO STUDENTS3 VALUES("Arix", "Machine Learning", "B")''')
cursor.execute('''INSERT INTO STUDENTS3 VALUES("Ana", "Devops", "A")''')
cursor.execute('''INSERT INTO STUDENTS3 VALUES("Harry", "Data Science", "B")''')
cursor.execute('''INSERT INTO STUDENTS3 VALUES("Ninja", "Deep Learning", "C")''')

# Commit the changes to save the records
connection.commit()

# Display all the records
print("Inserted records are:\n")
data = cursor.execute('''SELECT * FROM STUDENTS3''')
for row in data:
    print(row)

# Close the connection
connection.close()





