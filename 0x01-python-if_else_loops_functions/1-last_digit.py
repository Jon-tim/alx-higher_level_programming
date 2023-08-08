#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    last_digit_of_number = number % 10
else:
    last_digit_of_number = ((number * -1) % 10) * -1

output = "Last digit of {} is {} and is".format(number, last_digit_of_number)

if last_digit_of_number > 5:
    print(output, "greater than 5")
elif last_digit_of_number == 0:
    print(output, "0")
else:
    print(output, "less than 6 and not 0")
