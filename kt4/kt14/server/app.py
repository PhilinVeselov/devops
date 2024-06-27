from flask import Flask, render_template, request, jsonify
import sqlite3
from flask_cors import CORS  # Импортируем Flask-CORS

app = Flask(__name__)

# SQLite setup
conn = sqlite3.connect('drivers.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS drivers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fio TEXT NOT NULL,
        passport TEXT NOT NULL,
        experience INTEGER NOT NULL,
        category TEXT NOT NULL
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS cars (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        driver_id INTEGER,
        license_plate TEXT NOT NULL,
        brand TEXT NOT NULL,
        year INTEGER NOT NULL,
        FOREIGN KEY (driver_id) REFERENCES drivers (id)
    )
''')
conn.commit()
conn.close()
app = Flask(__name__)
CORS(app)
# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/drivers', methods=['GET'])
def get_drivers():
    conn = sqlite3.connect('drivers.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM drivers')
    drivers = cursor.fetchall()
    conn.close()
    return jsonify({'drivers': drivers})

# В файле вашего Flask-приложения (обычно app.py)

@app.route('/driver_cars/<int:driver_id>', methods=['GET'])
def get_driver_cars(driver_id):
    conn = sqlite3.connect('drivers.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cars WHERE driver_id = ?', (driver_id,))
    cars = cursor.fetchall()
    conn.close()
    return jsonify({'cars': cars})

# В файле вашего Flask-приложения (обычно app.py)

@app.route('/add_car/<int:driver_id>', methods=['POST'])
def add_car(driver_id):
    data = request.get_json()
    license_plate = data['licensePlate']
    brand = data['brand']
    year = data['year']

    conn = sqlite3.connect('drivers.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO cars (driver_id, license_plate, brand, year) VALUES (?, ?, ?, ?)',
                   (driver_id, license_plate, brand, year))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Car added successfully'})


@app.route('/add_driver', methods=['POST'])
def add_driver():
    data = request.get_json()
    fio = data['fio']
    passport = data['passport']
    experience = data['experience']
    category = data['category']

    conn = sqlite3.connect('drivers.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO drivers (fio, passport, experience, category) VALUES (?, ?, ?, ?)',
                   (fio, passport, experience, category))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Driver added successfully'})

# Добавьте аналогичные роуты для обновления и удаления водителя, а также для добавления, обновления и удаления автомобиля
@app.route('/update_driver/<int:driver_id>', methods=['PUT'])
def update_driver(driver_id):
    data = request.get_json()
    fio = data['fio']
    passport = data['passport']
    experience = data['experience']
    category = data['category']

    conn = sqlite3.connect('drivers.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE drivers SET fio=?, passport=?, experience=?, category=? WHERE id=?',
                   (fio, passport, experience, category, driver_id))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Driver updated successfully'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
