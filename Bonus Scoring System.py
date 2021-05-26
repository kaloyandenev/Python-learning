import math
max_bonus_points = 0
max_points_attendance = 0

# четем от конзолата брой студенти, брой лекции
students_count = int(input())
course_lectures = int(input())
initial_bonus = int(input())
# for цикъл за всеки студент с диапазон броя на студентите
for student in range(students_count):
    # четем брой лекции
    student_attendances = int(input())
# изчисляваме current_bonus_points за всеки студент по формула
    current_bonus_points = student_attendances / course_lectures * (5 + initial_bonus)
# if проверка дали current_bonus_points > max_bonus_points
    if current_bonus_points > max_bonus_points:
        max_bonus_points = current_bonus_points
        max_points_attendance = student_attendances

# запазваме резултата в променлива и запазваме броя лекции
# принтираме Max bonus брой лекции
print(f"Max Bonus: {math.ceil(max_bonus_points)}.")
print(f"The student has attended {max_points_attendance} lectures.")
