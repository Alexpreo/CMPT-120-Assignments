import sys

while True:
    question1 = input('Hi, this is Pchatbot, can I talk to you?\n')

    if question1 == 'Y' or question1 == 'y':
        question2 = input('What is your name?\n')
        print("Nice to meet you, " + question2 + ".")
        break
    elif question1 == 'N' or question1 == 'n':  
        print('Okay! Talk to you soon!')
        sys.exit()
    else:
        print("Please answer only 'Y' or 'N'\n")

positive = ['Good', 'I’m great', 'I’m good' 'Fine',]
negative = ['Bad', 'Not Okay', "I'm feeling good"]
    
question3 = input('How are you doing today?\n')
    
if question3 in positive:
    print("I'm glad you're feeling well, " + question2 + '.')
elif question3 in negative:
    print('Have some time to yourself to recharge!')
else:
    print('I see!')
    
question4 = int(input('How old are you?\n'))
if question4 > 18 and question3 in positive:
    print('You are ready to drive.')
else:
    print('Still taking the bus!')