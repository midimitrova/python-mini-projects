def add(a, b):
    answer = a + b
    print(str(a) + ' + ' + str(b) + ' = ' + str(answer) + '\n')


def subtract(a, b):
    answer = a - b
    print(str(a) + ' - ' + str(b) + ' = ' + str(answer) + '\n')


def multiplication(a, b):
    answer = a * b
    print(str(a) + ' * ' + str(b) + ' = ' + str(answer) + '\n')


def division(a, b):
    answer = a / b
    print(str(a) + ' / ' + str(b) + ' = ' + str(answer) + '\n')


while True:
    print('Choose A for Addition')
    print('Choose B for Subtraction')
    print('Choose C for Multiplication')
    print('Choose D for Division')
    print('Choose E for Exit')

    choice = input("Please, choose from A to E: ").upper()

    if choice == 'A':
        print('Addition')
        a = input('input first number: ')
        b = input('input second number: ')
        if not a.isdigit() or not b.isdigit():
            print('Please, enter numbers!\n')
            a = input('input first number: ')
            b = input('input second number: ')
            if a.isdigit() and b.isdigit():
                add(int(a), int(b))
        else:
            add(int(a), int(b))

    elif choice == 'B':
        print('Subtraction')
        a = input('input first number: ')
        b = input('input second number: ')
        if not a.isdigit() or not b.isdigit():
            print('Please, enter numbers!\n')
            a = input('input first number: ')
            b = input('input second number: ')
            if a.isdigit() and b.isdigit():
                subtract(int(a), int(b))
        else:
            subtract(int(a), int(b))
    elif choice == 'C':
        print('Multiplication')
        a = input('input first number: ')
        b = input('input second number: ')
        if not a.isdigit() or not b.isdigit():
            print('Please, enter numbers!\n')
            a = input('input first number: ')
            b = input('input second number: ')
            if a.isdigit() and b.isdigit():
                multiplication(int(a), int(b))
        else:
            multiplication(int(a), int(b))
    elif choice == 'D':
        print('Division')
        a = input('input first number: ')
        b = input('input second number: ')
        if not a.isdigit() or not b.isdigit():
            print('Please, enter numbers!\n')
            a = input('input first number: ')
            b = input('input second number: ')
            if a.isdigit() and b.isdigit():
                if int(b) == 0:
                    print('You can not divide by zero!\n')
                else:
                    division(int(a), int(b))
        else:
            if int(b) == 0:
                print('You can not divide by zero!\n')
            else:
                division(int(a), int(b))
    elif choice == 'E':
        print('Program ended!')
        quit()
