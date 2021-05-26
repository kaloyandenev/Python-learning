courses = {}
command = input()

while not command == "end":
    course, student = command.split(" : ")
    if course not in courses:
        courses[course] = []
        courses[course].append(student)
    else:
        courses[course].append(student)

    command = input()

sorted_courses = sorted(courses.items(), key=lambda kvp: len(kvp[1]), reverse=True)

for course, students in sorted_courses:
    sorted_students = sorted(students)
    print(f"{course}: {len(students)}")
    for student in sorted_students:
        print(f"-- {student}")
