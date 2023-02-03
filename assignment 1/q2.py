operations = int(input("Hi, how many operations do you want MagiCal to perform?\n"))

for i in range(operations):
    choice = input("Select the operator from the list of Addition (1), Subtraction (2), Multiplication (3), Division (4):\n")
    if choice == '1' or choice == '2' or choice == '3' or choice == '4':
        num1 = int(input("Enter the first number in the interval of [0,100]:\n"))
        num2 = int(input("Enter the second number in the interval of [0,100]:\n"))
        if 0 <= num1 <= 100 and 0 <= num2 <= 100:
            if choice == '1':
                print(num1, '+', num2, '=', (num1 + num2))
            elif choice == '2':
                print(num1, '-', num2, '=', (num1 - num2))
            elif choice == '3':
                print(num1, '*', num2, '=', (num1 * num2))                
            elif choice == '4':  
                if num2 == 0:
                    print("The denominator cannot be 0.")  
                else:
                    print(num1, '/', num2, '=', (num1 / num2))
            else:
                print("Invalid input!")
        else:
            print("Magic calculator can not perform your operation!")
    else:
        print("Invalid input!")          