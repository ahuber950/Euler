# porblem 5

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# define function for listing primary factors


def pfacs(num):
    primes = []
    for i in range(2, num + 1):
        while num % i == 0:
            primes.append(i)
            num /= i
        if num == 1:
            break
    return primes


def prod(list):
    p = 1
    for i in list:
        p *= i
    return p


def mod5(num):

    if type(num) != int or num < 1:
        raise ValueError("The value must be an integer greater than zero")

    min_facs = []
    for i in range(2, num + 1):
        facs_facs = pfacs(i)
        for j in facs_facs:
            while facs_facs.count(j) > min_facs.count(j):
                min_facs.append(j)
                min_facs.sort()

    p = prod(min_facs)
    return p
