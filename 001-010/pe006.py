# Problem 6

# The sum of the squares of the first ten natural numbers is,
# 1**2 + 2**2 + ... + 10**2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)**2 = 55**2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import math

# define function for squaring a sum of numbers
def sum_squares(limit_susq):
    sum = 0
    for i in range(int(limit_susq) + 1):
        sum += i ** 2
    return sum


# define function for summing squares of numbers
def square_sum(limit_sqsu):
    sum = 0
    for i in range(int(limit_sqsu) + 1):
        sum += i
    return sum ** 2


def mod6(limit_mod):

    if type(limit_mod) != int or limit_mod < 1:
        raise ValueError("The value must be an integer greater than zero")

    return square_sum(limit_mod) - sum_squares(limit_mod)
