# password Generator
import random
import string

print('----------------PASSWORD GENERATOR-------------------')

print('''We will help you to generate 3 types of passwords
1. Weak passwords : It will consist 4 alphabets.
2. Moderate passwords: It will consist 7 alphanumeric characters.
3. Strong Passwords : It will consist 10 alphanumeric and symbol characters.''')


while True:
    user_input = input('''
What type of password you need?
Enter "W" for weak password
Enter "M" for moderate password
Enter "S" for strong password\n''')

    # To reduce chances of error if user gives command in upper or lower case.
    user_input = user_input.lower()


    if user_input == 'w':
        alphabet = string.ascii_letters # string.digits + string.punctuation
        password = ''.join(random.choice(alphabet) for i in range(4))
        print(password)
        break

    elif user_input == 'm':
        alphabet = string.ascii_letters + string.digits # string.punctuation
        password = ''.join(random.choice(alphabet) for i in range(7))
        print(password)
        break

    elif user_input == 's':
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(alphabet) for i in range(10))
        print(password)
        break

    else:
        print('Please enter a valid choice')
