from turtle import delay

x = -100
while x < 0:
    if (x ** 2 + 1) % 4 == 0:
        print(x)
        print(True)
        x += 1

    else:
        print(x)
        print(False)
        x += 1

