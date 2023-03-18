import os
def compute_avg_grade(course):

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, "grades.txt")
    with open(file_path) as f:
        lines = f.readlines()

    grades = []
    for line in lines:
        dept, course_num, student_num, grade = line.split()
        
        if dept == course[0] and course_num == course[1]:
            grades.append(int(grade))

    avg = sum(grades) / len(grades)

    print("{:.2f}".format(avg))


def compute_gpa(student_num):

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, "grades.txt")
    with open(file_path) as f:
        lines = f.readlines()

    grades = []
    for line in lines:
        dept, course_num, stud_num, grade = line.split()

        if stud_num == student_num:
            grades.append(int(grade))

    gpa = sum(grades) / len(grades)

    print("{:.2f}".format(gpa))


def count_failed_students(course):

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, "grades.txt")

    with open(file_path) as f:
        lines = f.readlines()

    num_failed = 0
    for line in lines:
        dept, course_num, stud_num, grade = line.split()

        if dept == course[0] and course_num == course[1] and int(grade) < 75:
            num_failed += 1
    print(num_failed)


while True:
    user_input = input().split()

    if user_input[0] == 'avg':
        compute_avg_grade(user_input[1:])
    elif user_input[0] == 'gpa':
        compute_gpa(user_input[1])
    elif user_input[0] == 'fails':
        count_failed_students(user_input[1:])
    elif user_input[0] == 'quit':
        break
