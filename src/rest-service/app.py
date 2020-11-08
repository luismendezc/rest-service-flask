from flask import Flask, jsonify, abort, request

app = Flask(__name__)

students = [
    {
        "id": 1,
        "first_name": "leon",
        "last_name": "hess",
        "mat_nr": 12345
    },
    {
        "id": 2,
        "first_name": "kai",
        "last_name": "dieter",
        "mat_nr": 54321
    }
]


@app.route('/api/students', methods=['GET'])
def get_students():
    return jsonify({"students": students})


@app.route('/api/student/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = [student for student in students if student["id"] == student_id]
    if len(student) == 0:
        abort(404)
    return jsonify({"student": student[0]})


@app.route('/api/students', methods=['POST'])
def create_student():
    if not request.json:
        abort(400)
    if len(students) != 0:
        id = students[-1]["id"] + 1
    else:
        id = 1

    student = {
        "id": id,
        "first_name": request.json["first_name"],
        "last_name": request.json["last_name"],
        "mat_nr": request.json["mat_nr"]
    }
    students.append(student)
    return jsonify({"student": student})


@app.route('/api/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = [student for student in students if student['id'] == student_id]
    if len(student) == 0:
        abort(404)
    if not request.json:
        abort(400)

    student[0]["first_name"] = request.json.get("first_name", student[0]["first_name"])
    student[0]["last_name"] = request.json.get("last_name", student[0]["last_name"])
    student[0]["mat_nr"] = request.json.get("mat_nr", student[0]["mat_nr"])
    return jsonify({"student": student[0]})


@app.route('/api/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = [student for student in students if student["id"] == student_id]
    if len(student) == 0:
        abort(404)
    students.remove(student[0])
    return jsonify({"result": True})


if __name__ == '__main__':
    app.run(port=2000, host="0.0.0.0")
