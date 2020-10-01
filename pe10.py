# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

import time

st = time.time()

not_prime = set()
prime = set()
num = 2000000

for i in range(2, num):
    if i not in not_prime:
        prime.add(i)
        for j in range(i, (num // i) + 1):
            not_prime.add(i * j)
            if i == 5:
                print(i * j)


print(sum(prime))
end = time.time()

print("this code took ", str(end - st), " seconds to run")
