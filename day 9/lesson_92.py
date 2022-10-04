student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if 90 < score < 101:
        student_grades[student] = "Outstanding"
    elif 80 < score < 91:
        student_grades[student] = "Exceeds Expectations"
    elif 70 < score < 81:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)
