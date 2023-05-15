from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

students = {}

@app.route('/students', methods=['POST'])
def add_student():
    data = request.json
    student_id = data['student_id']
    students[student_id] = data
    return jsonify({'message': 'Student added successfully!'})

@app.route('/students/<student_id>', methods=['GET'])
def get_student(student_id):
    if student_id in students:
        return jsonify(students[student_id])
    else:
        return jsonify({'message': 'Student not found'}), 404

@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'student_id': request.form['student_id'],
            'average_grade': request.form['average_grade']
        }
        students[data['student_id']] = data
        return jsonify({'message': 'Student added successfully!'})
    else:
        return render_template('html.html')

if __name__ == '__main__':
    app.run()
