# 🎓 Student Performance Analyzer

> A Python CLI tool that collects student marks, calculates total, percentage, grade, and result, and saves records to a JSON database — clean OOP design, no external dependencies.

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Terminal%20%2F%20CLI-black?style=for-the-badge&logo=gnubash&logoColor=white)]()

---

## ✨ Features

| Feature | Description |
|---|---|
| 📋 **Student Registration** | Enter name, roll number, branch, and semester |
| 📝 **Dynamic Subject Entry** | Add any number of subjects with custom names and marks |
| 🧮 **Smart Calculations** | Total marks, percentage, A+/A/B/C/D/F grade, Pass/Fail result |
| 🏆 **Top/Bottom Subject** | Instantly identifies highest and lowest scoring subject |
| 💾 **Persistent Storage** | Appends every record to `data/students.json` for future reference |
| 🧩 **Clean OOP Architecture** | Separate modules: `Student` class, `analysis.py`, `data.py` |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.x installed ([download here](https://python.org/downloads))
- No external libraries required — uses only Python standard library

### Run the App
```bash
# 1. Clone the repository
git clone https://github.com/akashcyber02/Student-Performance-Analyzer.git
cd Student-Performance-Analyzer

# 2. Run the analyzer
python app.py
```

### Example Session
```
===== Student Performance Analyzer =====
Enter student name: Akash Dhakad
Enter roll number: 0901CS221002
Enter branch: CSE
Enter semester: 4

Student details added successfully!

Enter number of subjects: 3
Enter subject name: Mathematics
Enter marks: 85
Enter subject name: Physics
Enter marks: 72
Enter subject name: Programming
Enter marks: 91

================================
       PERFORMANCE REPORT
================================
Student: Akash Dhakad
Roll Number: 0901CS221002
Branch: CSE
Semester: 4

Subjects and Marks:
Mathematics : 85.0
Physics : 72.0
Programming : 91.0

Total Marks: 248.0
Percentage: 82.67 %
Grade: A
Result: Pass

Highest Scoring Subject: Programming - 91.0
Lowest Scoring Subject: Physics - 72.0
================================

Student data saved successfully!
```

---

## 📁 Project Structure

```
Student-Performance-Analyzer/
├── app.py          # Main entry point — input collection & report printing
├── student.py      # Student class definition (OOP model)
├── analysis.py     # Pure functions: total, percentage, grade, result, best/worst subject
├── data.py         # JSON persistence — save_student() appends to data/students.json
├── data/
│   └── students.json   # Persistent student records database
└── requirements.txt    # Empty — zero external dependencies
```

---

## 🔬 Grading System

| Percentage Range | Grade |
|:---:|:---:|
| ≥ 90% | A+ |
| ≥ 80% | A |
| ≥ 70% | B |
| ≥ 60% | C |
| ≥ 50% | D |
| < 50% | F (Fail) |
| < 40% | Fail |

---

## 🛠️ Tech Stack

- **Language**: Python 3.x
- **Architecture**: Object-Oriented Programming (OOP)
- **Storage**: JSON file (`data/students.json`)
- **Dependencies**: None (pure standard library)

---

## 📈 Future Improvements

- [ ] Web UI using Streamlit or Flask
- [ ] CSV/PDF export of student reports
- [ ] Batch import from CSV
- [ ] Subject-wise graph visualization (matplotlib)
- [ ] Multi-semester tracking per student

---

## 👨‍💻 Author

**Akash Dhakad**
- GitHub: [@akashcyber02](https://github.com/akashcyber02)

---

## 📄 License

This project is open source under the [MIT License](LICENSE).
