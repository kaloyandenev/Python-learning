students_grades = {}
language_submissions = {}
command = input()
while not command == "exam finished":
    test_command = command.split("-")
    if len(test_command) == 3:
        student, language, grade = command.split("-")
        grade = int(grade)
        for user in students_grades:
            if student == user:
                if students_grades[student] <= grade:
                    students_grades[student] = grade
        if student not in students_grades:
            students_grades[student] = grade
        if language not in language_submissions:
            language_submissions[language] = 1
        else:
            language_submissions[language] += 1

    if len(test_command) == 2:
        command = command.split("-")
        student = command[0]
        students_grades.pop(student)

    command = input()
print(f"Results:")
sorted_students = dict(sorted(students_grades.items(), key=lambda kvp: (-kvp[1], kvp[0])))
sorted_languages = dict(sorted(language_submissions.items(), key=lambda kvp: (-kvp[1], kvp[0])))

# print(sorted_students)
# print(sorted_languages)
for student in sorted_students:
    print(f"{student} | {sorted_students[student]}")
print(f"Submissions:")
for language in sorted_languages:
    print(f"{language} - {sorted_languages[language]}")
