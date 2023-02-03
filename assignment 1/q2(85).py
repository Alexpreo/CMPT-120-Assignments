operations = int(input("Hi, how many operations do you want MagiCal to perform?\n"))

for i in range(operations):
    choice = input("Select the operator from the list of Addition (1), Subtraction (2), Multiplication (3), Division (4):\n")

    if choice == '1':
        num1 = int(input("Enter the first number in the interval of [0,100]:\n"))
        num2 = int(input("Enter the second number in the interval of [0,100]:\n"))
        if num1 >= 100 or num1 <= 0:
            print("Magic calculator can not perform your operation!")
        if num2 >= 100 or num2 <= 0:
            print("Magic calculator can not perform your operation!")
        else:
            num3 = num1 + num2
            print(num1, "+", num2, "=", num3)
        
    elif choice == '2':
        num1 = int(input("Enter the first number in the interval of [0,100]:\n"))
        num2 = int(input("Enter the second number in the interval of [0,100]:\n"))
        if num1 >= 100 or num1 <= 0:
            print("Magic calculator can not perform your operation!")
        if num2 >= 100 or num2 <= 0:
            print("Magic calculator can not perform your operation!")
        else:
            num3 = num1 - num2
            print(num1, "-", num2, "=", num3)
        
    elif choice == '3':
        num1 = int(input("Enter the first number in the interval of [0,100]:\n"))
        num2 = int(input("Enter the second number in the interval of [0,100]:\n"))
        if num1 >= 100 or num1 <= 0:
            print("Magic calculator can not perform your operation!")
        if num2 >= 100 or num2 <= 0:
            print("Magic calculator can not perform your operation!")
        else:
            num3 = num1 * num2
            print(num1, "*", num2, "=", num3)
        
    elif choice == '4':
        num1 = int(input("Enter the first number in the interval of [0,100]:\n"))
        num2 = int(input("Enter the second number in the interval of [0,100]:\n"))
        if num1 >= 100 or num1 < 0:
            print("Magic calculator can not perform your operation!")
        if num2 >= 100 or num2 < 0: 
            print("Magic calculator can not perform your operation!")
        if num2 == 0:
            print("The denominator cannot be 0.")
        else:
            num3 = num1 / num2
            print(num1, "/", num2, "=", num3)
    else:
        print("Invalid input!")