# Student Management System

A simple command-line based **Student Management System** built using **Python** and **MySQL**.
This project allows users to perform basic CRUD (Create, Read, Update, Delete) operations on student records.

---

## Features

* Add new students
* View all students
* Update student details
* Delete student records
* Automatic database and table creation

---

## Technologies Used

* Python 3
* MySQL
* `mysql-connector-python`

---

## Project Structure

```bash
student_management_system/
│
├── main.py
└── README.md
```

---

## Database Details

### Database Name

```sql
student_db
```

### Table Name

```sql
student
```

### Table Schema

| Column Name | Data Type                         |
| ----------- | --------------------------------- |
| id          | INT (Primary Key, Auto Increment) |
| name        | VARCHAR(100)                      |
| age         | INT                               |
| mark        | INT                               |
| created_at  | TIMESTAMP                         |
| updated_at  | TIMESTAMP                         |

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/student-management-system.git
cd student-management-system
```

### 2. Install Required Package

```bash
pip install mysql-connector-python
```

### 3. Configure MySQL

Make sure MySQL server is running.

Update the database credentials in the code if needed:

```python
host="127.0.0.1",
user="root",
password="root123"
```

---

## Running the Project

```bash
python main.py
```

---

## Menu Options

```text
-------STUDENT-MANAGEMENT-SYSTEM--------
1. Add Students
2. View Students
3. Update Student
4. Delete Student
5. Exit
```

---

## Example Output

### Add Student

```text
enter name: John
enter age: 20
enter marks: 85
```

### View Students

```text
id:1 | name:John | age:20 | mark:85
```

---

## Functions Overview

| Function           | Description                  |
| ------------------ | ---------------------------- |
| `init_db()`        | Creates database and table   |
| `get_connection()` | Establishes MySQL connection |
| `add_student()`    | Adds new student             |
| `view_students()`  | Displays all students        |
| `update_student()` | Updates student information  |
| `delete_student()` | Deletes a student record     |
| `menu()`           | Displays CLI menu            |

---
