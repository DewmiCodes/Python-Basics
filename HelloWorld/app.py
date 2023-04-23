print("Dewmi Samaradiwakara")
print("0----")
print(" ////")
print("*" * 10)

price = 10
rating = 4.9
is_published = True
print (price)

name = ("John Smith")
age = ("20 years")
is_new = True
print(name, age, is_new)

#name = input("What is your name? ")
#favorite_color = input("What is your favorite color? ")
#print(name + " likes " + favorite_color)

#birth_year = input("Birth year: ")
#print(type(birth_year))
#age = 2023 - int(birth_year)
#print(type(age))
#print(age)

#weight = input("What is your weight in pounds? ")
#weight_in_kilograms = int(weight) * 10
#print(weight_in_kilograms)

#course = '''
#Hi Harishi
#Here is our first date
#Thank you,
#Yours Dewmi
#'''
#print(course)

course = 'Python for Beginners'
print(course[0:4])

first = "Harisi"
second = "Burusi"
message = first + " [" + second + "] is a coder"
msg = f"{first} [{second}] is a coder"
print(msg)

course = "Swedish for Immigrants"
print(len(course))
print(course.upper())
print(course.lower())
print(course)
print(course.find("m"))
print(course.replace("Immigrants", "Harisi"))
print("for" in course)

print(40 / 3)
print(40 // 3)
print(40 % 6)
print(20 ** 3)

x=15
x=x+5
print(x)

x=10
x-=3
print(x)

x=10
x+=5
print(x)

x = 10 + 3 * 2 ** 2
print(x)

x=(2+3)*10-3
print(x)

x = 7.6
print(round(x))

x = 7.6
print(abs(-3))

import math
print(math.floor(4.9))

is_hot = False
is_cold = False
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")

price = 1000000
good_credit = False
if good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"down_payment: ${down_payment}")

#Logical Operators
has_high_income = True
has_good_credit = False
if has_high_income or has_good_credit:
    print("Eligible for loan")

has_good_credit = True
has_criminal_record = False
if has_good_credit and not has_criminal_record:
    print("Eligible for loan")

#Comparison Operators
temperature = 30
if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

name = "Dewmi"
if len(name) < 3:
    print("Name must be at least 3 characters.")
elif len(name) > 50:
    print("name must be a maximum of 50 characters")
else:
    print("Name looks good!")

#Project: Weight Converter
#weight = int(input("Weight: "))
#unit = input("(L)bs or (K)g: ")
#if unit.upper() == "L":
#    converted = weight * 0.45
#    print(f"You are {converted} kilos")
#else:
#    converted = weight / 0.45
#    print(f"You are {converted} pounds")

#While Loops
i = 1
while i <= 5:
    print(i)
    i = i + 1
print("Done")

i = 1
while i <= 5:
    print("*" * i)
    i = i + 1
print("Done")

#Guessing Game
secret_number =9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You Won!")
        break
else:
    print("sorry, you failed")

#Car Game



























