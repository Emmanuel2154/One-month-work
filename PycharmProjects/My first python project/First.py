print("Emmanuel")
print('*' * 10)

# input....to receive info from user
name = input('What is your name? ')
print('Hi ' + name)  # applying concatenation
color = input('What is your favorite color? ')
print(name + ' likes ' + color)

# type conversion(int, boolean, string etc.)
birth_year = input('Birth year: ')
print(type(birth_year))
age = 2025 - int(birth_year)
print(age)

# practice.....asking the user for their age, converting it to kilograms and printing on the terminal
weight_in_pounds = input('Weight: ')
weight_in_kilograms = int(weight_in_pounds) * 0.453592
print(weight_in_kilograms)

# characteristics of strings
# triple quotes
'''
Hi Emmanuel,
Here is our first Email to you
Thank you,
The support team
'''
# use of index
course = 'Python learning'
print(course[0:3])
print(course[0:])
print(course[:5])
another = course[:]
print(course[1:-1])

# formatted strings
first_name = 'Emmanuel'
last_name = 'Nwokoma'
message = first_name + ' [' + last_name + '] is a coder'
msg = f'{first_name} [{last_name}] is a coder'
print(message)
print(msg)

# calculate number of character in a string
print(len(course))
# for uppercase
print(course.upper())

# for lowercase
print(course.lower())

# to find a particular character
print(course.find('P'))

# to replace character
print(course.replace('learning', 'for absolute Beginners'))

# to know if a particular character exists in a class
print('Print' in course)

# math functions
x = -3.15
print(abs(x))

# if statements
is_hot = True
is_cold = True
if is_hot:
    print("It's a hot day")
    print('Drink plenty of water')
elif is_cold:
    print("It's a cold day")
    print('Wear warm clothes')
else:
    print("It's a lovely day")
print("Enjoy your day")

# program that displays the down payment of a buyer
price = 100000
is_good_credit = False

if is_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")

# Logical operators
has_high_income = True
has_good_credit = False

if has_high_income and not has_good_credit:
    print('Eligible')

# comparison operators
temperature = 30

if temperature > 20:
    print("It's a hot day")
else:
    print("It's not a hot day")

user_name = input('Enter your name: ')
number_characters = len(user_name)
if number_characters < 3:
    print("Name must be at least 3 characters")
elif number_characters > 50:
    print("Name can be maximum of 50 characters")
else:
    print("Name looks good")

# project on weight conversion
weight = int(input('Enter weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")

# while loops
i = 1
while i <= 5:
    print(i)
    i += 1
print("Done")
# Practice
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
        break
else:
    print("You failed")

# another project
user_command = ""
entered_command = set()
while True:
    user_command = input("> ").lower()
    if user_command in entered_command:
        if user_command == "start":
            print("Car has already started")
        elif user_command == "stop":
            print("Car has already stopped")
    else:
        entered_command.add(user_command)
        if user_command == "start":
            print("Car has started")
        elif user_command == "stop":
            print("Car has stopped")
        elif user_command == "help":
            print("""
            start - to start the car
            stop - to stop the car
            quit - to exit
            """)
        else:
            print("Sorry, I don't understand")
