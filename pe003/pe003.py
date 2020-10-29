# Problem 3

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


def mod3(num):

    if type(num) != int or num < 2:
        raise ValueError("The value must be an integer greater than 1")

    import math

    prime_min = 2
    prime_max = math.ceil(math.sqrt(num) + 1)
    primes = [num]

    for i in range(prime_min, prime_max):
        if primes[0] == 1:
            break
        while primes[0] % i == 0:
            primes.append(i)
            primes[0] = primes[0] / i
    return max(primes)
