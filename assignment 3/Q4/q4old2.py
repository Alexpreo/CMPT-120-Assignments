import os
# define function to compute the average grade of a specific course
def compute_avg_grade(course_grades):
    grades_sum = 0
    num_grades = len(course_grades)
    for grade in course_grades:
        grades_sum += grade
    return grades_sum / num_grades


dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(dir_path, "grades.txt")

# read grades.txt file
with open(file_path, 'r') as f:
    grades = {}
    for line in f:
        department, course_number, student_number, grade = line.split()
        course = department + ' ' + course_number
        if course not in grades:
            grades[course] = []
        grades[course].append(int(grade))

# process user commands
while True:
    command = input().split()

    # compute average grade of a specific course
    if command[0] == "avg":
        course = ' '.join(command[1:])
        avg_grade = compute_avg_grade(grades[course])
        print("{:.2f}".format(avg_grade))

    # compute GPA of a specific student
    elif command[0] == "gpa":
        student_grades = []
        with open(file_path, 'r') as f:
            for lines in f:
                depart, course_num, stu_num, grd = lines.split()
                print(lines)
                if command[1] == stu_num:
                    student_grades.append(int(lines[4]))
                    print(student_grades)
        gpa = compute_avg_grade(student_grades)
        print("{:.2f}".format(avg_grade))

    # count number of failed students of a specific course
    elif command[0] == 'fails':
        course = ' '.join(command[1:])
        count = 0
        for grade in grades[course]:
            if grade < 75:
                count += 1
        print(count)

    # exit program
    elif command[0] == 'quit':
        break

    # invalid command
    else:
        print('Invalid command.')
