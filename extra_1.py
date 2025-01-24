grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted_students = sorted(students)
print(sorted_students)

for student, grade_list in zip(sorted_students, grades):
    print(student, grade_list)

average_grades = {
    student: sum(grade_list) / len(grade_list)
    for student, grade_list in zip(sorted_students, grades)
}
print(average_grades)