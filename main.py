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



def update_student():
    conn = get_connection()
    cursor = conn.cursor()

    student_id = int(input("Enter student id: "))
    new_name = input("Enter the new name: ")
    new_age = int(input("Enter new age: "))
    new_mark = int(input("Enter new mark: "))

    query = """
        UPDATE student 
        SET name=%s, age=%s, mark=%s
        WHERE id=%s
    """
    values = (new_name, new_age, new_mark, student_id)

    cursor.execute(query,values)
    conn.commit()
    conn.close()


def delete_student():
    conn = get_connection()
    cursor = conn.cursor()

    student_id = int(input("Enter the student ID to delete: "))
    query = """
    DELETE FROM student
    WHERE id=%s
    """
    values = (student_id),

    cursor.execute(query,values)
    conn.commit()

    print("student deleted successfully")
    conn.close()

def menu():
    while True:
        print("\n-------STUDENT-MANAGEMENT-SYSTEM--------")
        print("1. Add Students")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        
        elif choice == "2":
            view_students()
        
        elif choice == "3":
            update_student()
        
        elif choice == "4":
            delete_student()
        
        elif choice == "5":
            print("Exiting...")
            break
        
        else:
            print("Invaild choice")

menu()