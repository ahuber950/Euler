# Problem 7

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

import math


def isprime(num):
    prime = True
    for i in range(2, math.ceil(math.sqrt(num)) + 1):
        if num % i == 0:
            prime = False
            break
    return prime


def mod7(x):

    if type(x) != int or x < 1:
        raise ValueError("The value must be an integer greater than zero")

    primes = [2]
    i = 3
    while len(primes) < x:
        if isprime(i) is True:
            primes.append(i)
        i += 2

    return primes[x - 1]
