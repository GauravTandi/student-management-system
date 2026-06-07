import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="root123",
        database="student_db"
    )

def add_student():
    conn = get_connection()
    cursor = conn.cursor()

    name = input("enter name: ")
    age = int(input("enter age: "))
    mark = int(input("enter marks: "))

    query = "INSERT INTO student (name, age, mark) VALUES (%s, %s, %s)"
    values = (name, age, mark)

    cursor.execute(query, values)
    conn.commit()
    conn.close()

def view_students():
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM student"
    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(f"id:{row[0]} | name:{row[1]} | age:{row[2]} | mark:{row[3]}")

    conn.close()