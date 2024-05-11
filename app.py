from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    students = fetch_students_from_db()
    return render_template('index.html', students=students)

def fetch_students_from_db():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('SELECT * FROM students')
    students = c.fetchall()
    conn.close()
    return students

if __name__ == '__main__':
    app.run(debug=True)
