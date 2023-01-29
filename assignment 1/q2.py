operations = int(input("Hi, how many operations do you want MagiCal to perform?\n"))
try:
    for i in range(operations):
        while True:
            operator = input("Select the operator from the list of Addition (1), Subtraction (2), Multiplication (3), Division (4):\n")
            if operator == '1':
                num1 = int(input("Enter the first number in the interval of [0,100]:\n"))
                num2 = int(input("Enter the second number in the interval of [0,100]:\n"))
                if num1 > 100 or num1 < 0:
                    print("Magic calculator can not perform your operation!")
                    break
                if num2 > 100 or num2 < 0:
                    print("Magic calculator can not perform your operation!")
                    break
                else:
                    num3 = num1 + num2
                    print(num1, "+", num2, "=", num3)
                    break
            if operator == '2':
                num1 = int(input("Enter the first number in the interval of [0,100]:\n"))
                num2 = int(input("Enter the second number in the interval of [0,100]:\n"))
                if num1 > 100 or num1 < 0:
                    print("Magic calculator can not perform your operation!")
                    break
                if num2 > 100 or num2 < 0:
                    print("Magic calculator can not perform your operation!")
                    break
                else:
                    num3 = num1 - num2
                    print(num1, "-", num2, "=", num3)
                    break
            if operator == '3':
                num1 = int(input("Enter the first number in the interval of [0,100]:\n"))
                num2 = int(input("Enter the second number in the interval of [0,100]:\n"))
                if num1 > 100 or num1 < 0:
                    print("Magic calculator can not perform your operation!")
                    break
                if num2 > 100 or num2 < 0:
                    print("Magic calculator can not perform your operation!")
                    break
                else:
                    num3 = num1 * num2
                    print(num1, "*", num2, "=", num3)
                    break
            if operator == '4':
                num1 = int(input("Enter the first number in the interval of [0,100]:\n"))
                num2 = int(input("Enter the second number in the interval of [0,100]:\n"))
                if num1 > 100 or num1 < 0:
                    print("Magic calculator can not perform your operation!")
                    break
                if num2 > 100 or num2 < 0:
                    print("Magic calculator can not perform your operation!")
                    break
                if num2 == 0:
                    print("The denominator cannot be 0.")
                    break
                else:
                    num3 = num1 / num2
                    print(num1, "/", num2, "=", num3)
                    break
            else:
                print("Invalid input!")

except EOFError as e:
    exit()
