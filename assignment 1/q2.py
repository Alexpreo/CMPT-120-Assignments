import sys

operations = int(input("Hi, how many operations do you want MagiCal to perform?\n"))

for i in range(operations):
    while True:
        operator = int(input("Select the operator from the list of Addition (1), Subtraction (2), Multiplication (3), Division (4):\n"))
        if 0 < operator < 5:
            num1 = int(input("Enter the first number in the interval of [0,100]:\n"))
            num2 = int(input("Enter the second number in the interval of [0,100]:\n"))
            if 0 > num1 > 100:
                print("Magic calculator can not perform your operation!")
            if 0 > num2 > 100:
                print("Magic calculator can not perform your operation!")
            else:
                pass
        else:
            print("Invalid input!")

sys.exit()
