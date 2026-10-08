import json

def save_student(student):
    data = {
        "name": student.name,
        "roll_no": student.roll_no,
        "branch": student.branch,
        "semester": student.semester,
        "subjects": student.subjects
    }

    with open("data/students.json", "r") as file:
        students = json.load(file)

    students.append(data)

    with open("data/students.json", "w") as file:
        json.dump(students, file, indent=4)