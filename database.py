import sqlite3

def create_database():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()

    # Create a table to store student data with the "myID" column
    c.execute('''CREATE TABLE IF NOT EXISTS students
                 (id INTEGER PRIMARY KEY,
                  name TEXT,
                  age INTEGER,
                  cgpa REAL,
                  myID TEXT)''')

    conn.commit()
    conn.close()

def insert_students(students_data):
    conn = sqlite3.connect('students.db')
    c = conn.cursor()

    # Delete all existing records
    c.execute('DELETE FROM students')

    # Insert new student records
    for student in students_data:
        c.execute('INSERT INTO students (name, age, cgpa, myID) VALUES (?, ?, ?, ?)', student)

    conn.commit()
    conn.close()

def fetch_all_students():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()

    c.execute('SELECT * FROM students')
    students = c.fetchall()

    conn.close()
    return students

if __name__ == '__main__':
    create_database()

    # Sample student data
    students_data = [
        ('mohamed ashraf abd el-hamid', 21, 3.0, '2106141'),
        ('marwan el shiekh', 19, 3.2, '20221324034'),
        ('mahmoud el abd', 21, 2.9, '210462'),
        ('mohamed ahmed', 20, 2.8, '20221311449'),
        ('mohamed ashraf ragab', 21, 2.8, '20221477329')
    ]

    insert_students(students_data)

    all_students = fetch_all_students()
    print(all_students)
