def calculate_total(subjects):
    total = sum(subjects.values())
    return total


def calculate_percentage(subjects):
    total = calculate_total(subjects)
    percentage = total / len(subjects)
    return percentage

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"
    
def check_result(percentage):
    if percentage >= 40:
        return "Pass"
    else:
        return "Fail"
def highest_subject(subjects):
    subject = max(subjects, key=subjects.get)
    return subject, subjects[subject]


def lowest_subject(subjects):
    subject = min(subjects, key=subjects.get)
    return subject, subjects[subject]   
