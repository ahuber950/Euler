# Problem 4

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


def mod4(digits):

    if type(digits) != int or digits < 1:
        raise ValueError("The value must be an integer greater than zero")

    x = 0

    for i in range(10 ** (digits - 1), 10 ** (digits)):
        for j in range(10 ** (digits - 1), 10 ** (digits)):
            if i * j > x and str(i * j) == str(i * j)[::-1]:
                x = i * j
    return x
