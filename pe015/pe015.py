# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


# How many such routes are there through a 20×20 grid?

def mod15(m, n, memo = None):
    if type(m) != int or m < 1 or type(n) != int or n < 1:
        raise ValueError("The dimensions must be integers greater than zero")

    if memo == None:
        memo = {}
    if m < n:
        m, n = n, m
    if str(m)+str(n) in memo:
        return memo[str(m)+str(n)]
    elif m == 1 or n == 1:
        result = 1
    else:
        result = mod15(m - 1, n, memo) + mod15(m, n - 1, memo)
    memo[str(m)+str(n)] = result
    return result

#solving for 21,21 becuase each square with side length n has n + 1 nodes by which to travel"

print(mod15(21,21))

