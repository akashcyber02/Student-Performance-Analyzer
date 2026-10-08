class Student:
    def __init__(self, name, roll_no, branch, semester):
        self.name = name
        self.roll_no = roll_no
        self.branch = branch
        self.semester = semester
        self.subjects = {}

    def add_subject(self, subject, marks):
        self.subjects[subject] = marks
        