from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Создаем базу данных и таблицу, если их нет
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER)''')
conn.commit()
conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM data")
    data = cursor.fetchall()
    conn.close()
    return render_template('index.html', data=data)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    age = request.form['age']
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO data (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    conn.close()
    return "Data added successfully!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

