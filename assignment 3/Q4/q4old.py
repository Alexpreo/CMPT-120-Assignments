import os

dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(dir_path, "grades.txt")

with open(file_path, "r") as f:
    grades = {}
    for line in f:
        department, course_number, student_number, grade = line.split()
        course = department + ' ' + course_number
        if course not in grades:
            grades[course] = []
        grades[course].append(int(grade))


def compute_average(grades):
    total = sum(grades)
    return total / len(grades)


while True:
    command = input().split()
    if command[0] == "avg":
        course = ' '.join(command[1:])
        avg_grade = compute_average(grades[course])
        print("{:.2f}".format(avg_grade))
    elif command[0] == "gpa":
        student_number = command[1]
        for course in grades:
            if student_number in course:
                grade = compute_average(grades[course])
        # print("{:.2f}".format(grade))
    elif command[0] == "fails":
        course = ' '.join(command[1:])
        count = 0
        for grade in grades[course]:
            if grade < 75:
                count += 1
        print(count)
    elif command[0] == "quit":
        break