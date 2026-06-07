import mysql.connector

def get_connection():
    db = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = "root123",
        database = "student_db")

    return db

def add_student():
    conn = get_connection()
    cursor = conn.cursor()

    name = input("enter name: ")
    age = int(input("enter age: "))
    marks = int(input("enter marks: "))

    query = "INSERT INTO student (name, age, mark) VALUES (%s, %s, %s)"
    values = (name, age, marks)

    cursor.execute(query, values)

    conn.commit()
    print("student added successfully.")
    conn.close()

add_student()