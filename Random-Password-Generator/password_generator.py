import random
import string

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


my_password = []

for char in range(nr_letters):
    my_password.append(random.choice(letters))

for sym in range(nr_symbols):
    my_password.append(random.choice(symbols))

for num in range(nr_numbers):
    my_password.append(random.choice(numbers))

random.shuffle(my_password)
print(''.join(my_password))