# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

# Values are in the associated text file

import numpy as np

def mod13(filename):

    if type(filename) != str or filename[-4:] != ".txt":
        raise ValueError("You must call a valid .txt file")

    vals = np.loadtxt(filename)

    return str(int(sum(vals)))[:10]

print(mod13("values.txt"))