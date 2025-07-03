import json
from flask import Flask, request, jsonify

app = Flask(__name__)
DATA_FILE = 'data.json'

def load_data():
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {
            'students': [],
            'courses': [],
            'enrollments': []
        }

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def get_next_id(items):
    if not items:
        return 1
    return max(item['id'] for item in items) + 1

@app.route('/students', methods=['GET'])
def list_students():
    data = load_data()
    return jsonify(data['students'])

@app.route('/students', methods=['POST'])
def add_student():
    data = load_data()
    students = data['students']
    new_student = {
        'id': get_next_id(students),
        'name': request.json.get('name')
    }
    students.append(new_student)
    save_data(data)
    return jsonify(new_student), 201

@app.route('/courses', methods=['GET'])
def list_courses():
    data = load_data()
    return jsonify(data['courses'])

@app.route('/courses', methods=['POST'])
def add_course():
    data = load_data()
    courses = data['courses']
    new_course = {
        'id': get_next_id(courses),
        'name': request.json.get('name')
    }
    courses.append(new_course)
    save_data(data)
    return jsonify(new_course), 201

@app.route('/enrollments', methods=['GET'])
def list_enrollments():
    data = load_data()
    return jsonify(data['enrollments'])

@app.route('/enrollments', methods=['POST'])
def add_enrollment():
    data = load_data()
    enrollments = data['enrollments']
    student_id = request.json.get('student_id')
    course_id = request.json.get('course_id')
    new_enrollment = {
        'student_id': student_id,
        'course_id': course_id
    }
    enrollments.append(new_enrollment)
    save_data(data)
    return jsonify(new_enrollment), 201

if __name__ == '__main__':
    app.run(debug=True)
