# Problem 10

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.


def mod10(num):

    import math

    if type(num) != int or num < 2:
        raise ValueError("The value must be an integer greater than zero")

    isprime = True
    primes = []
    if num > 2:
        primes.append(2)

    for i in range(3, num, 2):
        for j in primes:
            if i % j == 0:
                isprime = False
                break
            if j > i / j:
                break
        if isprime == True:
            primes.append(i)
        isprime = True

    return sum(primes)
