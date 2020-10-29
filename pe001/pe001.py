# Problem 1

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


def mod1(lim):

    if type(lim) != int:
        raise ValueError("The limit must be a non-negative integer")

    if lim < 0:
        raise ValueError("The limit must be a non-negative integer")

    sum = 0
    for i in range(1, lim):
        if i % 3 == 0 or i % 5 == 0:
            sum += i

    return sum
