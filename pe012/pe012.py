# Problem 12

# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# Let us list the factors of the first seven triangle numbers:

#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.

# What is the value of the first triangle number to have over five hundred divisors?


def mod12(num_divs):
    import math

    if type(num_divs) != int or num_divs < 1:
        raise ValueError("The value must be an integer greater than zero")

    trinum = 0.0
    counter = 0.0
    factors = []

    while len(factors) <= num_divs:
        counter += 1
        trinum = trinum + counter
        factors = [1.0, trinum]
        for i in range(2, int(math.ceil(math.sqrt(trinum)))):
            if trinum % i == 0:
                factors.append(i)
                factors.append(trinum / i)

        if math.sqrt(trinum) % 1 == 0:
            factors.append(math.sqrt(trinum))

    return trinum