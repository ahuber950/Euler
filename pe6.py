# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import math
import time

st = time.time()

# define function for squaring a sum of numbers
def sum_squares(num):
    sum = 0
    for i in range(int(num) + 1):
        sum += i ** 2
    return sum


# define function for summing squares of numbers
def square_sum(num):
    sum = 0
    for i in range(int(num) + 1):
        sum += i
    return sum ** 2


x = input(
    "I want the difference between the square of the sum\nand the sum of the squares of all numbers between 1 and __\n"
)

print(square_sum(x) - sum_squares(x))

end = time.time()
print(str(end - st) + " s")
