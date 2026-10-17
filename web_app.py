
import json
from pathlib import Path

import streamlit as st

# ---------- Page Configuration ----------
st.set_page_config(
    page_title="Student Performance Analyzer",
    page_icon="📊",
    layout="wide"
)

# ---------- Data File Location ----------
DATA_FILE = Path(__file__).parent / "data" / "students.json"


# ---------- Load Student Records ----------
def load_students():
    if not DATA_FILE.exists():
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            records = json.load(file)

        if isinstance(records, list):
            return [
                record for record in records
                if isinstance(record, dict)
            ]

        return []

    except (json.JSONDecodeError, OSError):
        st.error(
            "Student data could not be read. "
            "Please check data/students.json."
        )
        return []


# ---------- Calculate Student Percentage ----------
def get_percentage(student):
    subjects = student.get("subjects", {})

    if not isinstance(subjects, dict) or not subjects:
        return None

    try:
        marks = [float(value) for value in subjects.values()]

        if not all(0 <= mark <= 100 for mark in marks):
            return None

        return sum(marks) / len(marks)

    except (TypeError, ValueError):
        return None


# ---------- Dashboard ----------
st.title("📊 Student Performance Analyzer")
st.caption("Academic tracking • Performance insights • Student records")

st.divider()

students = load_students()

valid_percentages = [
    get_percentage(student)
    for student in students
]

valid_percentages = [
    percentage
    for percentage in valid_percentages
    if percentage is not None
]

all_subjects = set()

for student in students:
    subjects = student.get("subjects", {})

    if isinstance(subjects, dict):
        all_subjects.update(subjects.keys())


# ---------- Dashboard Metrics ----------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Students", len(students))

with col2:
    average = (
        sum(valid_percentages) / len(valid_percentages)
        if valid_percentages else 0
    )
    st.metric("Average Percentage", f"{average:.2f}%")

with col3:
    st.metric("Subjects Tracked", len(all_subjects))

st.divider()

# ---------- Student Records ----------
st.subheader("📋 Student Records")

if students:
    rows = []

    for student in students:
        percentage = get_percentage(student)

        rows.append({
            "Name": student.get("name", "N/A"),
            "Roll Number": student.get("roll_no", "N/A"),
            "Branch": student.get("branch", "N/A"),
            "Semester": student.get("semester", "N/A"),
            "Percentage": (
                f"{percentage:.2f}%"
                if percentage is not None
                else "Unavailable"
            )
        })

    st.dataframe(
        rows,
        use_container_width=True,
        hide_index=True
    )

else:
    st.info(
        "No student records found yet. "
        "Add a student to start analyzing performance."
    )

st.caption("Prototype version • Data source: students.json")
