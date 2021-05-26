number_of_students = int(input())
students = {}
for _ in range(number_of_students):
    student = input()
    grade = float(input())
    if student not in students:
        students[student] = [grade]
    else:
        students[student] += [grade]

students_high_grades = {}
for student in students:
    students[student] = sum(students[student]) / len(students[student])
    if students[student] >= 4.50:
        students_high_grades[student] = students[student]

sorted_students = sorted(students_high_grades.items(), key=lambda kvp: kvp[1], reverse=True)

for student, grade in sorted_students:
    print(f"{student} -> {grade:.2f}")
