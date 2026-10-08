from data import save_student
from student import Student
from analysis import (
    calculate_total,
    calculate_percentage,
    calculate_grade,
    check_result,
    highest_subject,
    lowest_subject
)

print("===== Student Performance Analyzer =====")

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
branch = input("Enter branch: ")
semester = int(input("Enter semester: "))

student = Student(name, roll_no, branch, semester)

print("\nStudent details added successfully!")

number_of_subjects = int(input("\nEnter number of subjects: "))

for i in range(number_of_subjects):
    subject = input("Enter subject name: ")
    marks = float(input("Enter marks: "))

    student.add_subject(subject, marks)


# CALCULATION OF TOTAL, PERCENTAGE, GRADE, RESULT, HIGHEST AND LOWEST SUBJECTS

total = calculate_total(student.subjects)
percentage = calculate_percentage(student.subjects)
grade = calculate_grade(percentage)
result = check_result(percentage)

highest = highest_subject(student.subjects)
lowest = lowest_subject(student.subjects)


# PERFORMANCE REPORT HAI

print("\n================================")
print("       PERFORMANCE REPORT")
print("================================")

print("Student:", student.name)
print("Roll Number:", student.roll_no)
print("Branch:", student.branch)
print("Semester:", student.semester)

print("\nSubjects and Marks:")

for subject, marks in student.subjects.items():
    print(subject, ":", marks)

print("\nTotal Marks:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)
print("Result:", result)

print("\nHighest Scoring Subject:", highest[0], "-", highest[1])
print("Lowest Scoring Subject:", lowest[0], "-", lowest[1])

print("================================")

save_student(student)

print("\nStudent data saved successfully!")