#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    last_digit_of_number = number % 10
else:
    last_digit_of_number = ((number * -1) % 10) * -1

if last_digit_of_number > 5:
    print(f"Last digit of {number} is {last_digit_of_number} and is greater than 5")
elif last_digit_of_number == 0:
    print(f"Last digit of {number} is {last_digit_of_number} and is 0")
else:
    print(f"Last digit of {number} is {last_digit_of_number} and is less than 6 and not 0")
