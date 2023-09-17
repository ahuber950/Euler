# Problem 9

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def mod9(desired_sum):

    import math

    if type(desired_sum) != int or desired_sum < 1:
        raise ValueError("The value must be an integer greater than zero")

    for c in range(1, math.ceil((desired_sum / 2 + 1))):
        for b in range(1, math.ceil((desired_sum / 4 + 1))):
            a = desired_sum - c - b
            if a ** 2 + b ** 2 == c ** 2 and b != c and a != c:
                return a * b * c

    return "No Pythagorean Triplet exists with that sum"
