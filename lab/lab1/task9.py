


def calculate_average_grades(grades):
    student_grades = {}
    for student, grade in grades:
        if student in student_grades:
            student_grades[student].append(grade)
        else:
            student_grades[student] = [grade]
    for student, grades in student_grades.items():
        average_grade = sum(grades) / len(grades)
        print(f"{student}'s average grade: {average_grade}")

grades = [("John", 80), ("Jane", 90), ("John", 70), ("Jane", 95), ("Jim", 60), ("Jim", 75)]
calculate_average_grades(grades)
