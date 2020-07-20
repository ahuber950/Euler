import math
import time
st=time.time()

def isprime(num):
	prime=True
	for i in range(2,math.ceil(math.sqrt(num))+1):
		if num%i==0:
			prime=False
			break
	return prime

x=int(input("I want to know the _th prime number\n"))
primes=[2]
i=3
while len(primes)<x:
	if isprime(i) is True:
		primes.append(i)
	i+=2

print(primes[x-1])
end=time.time()
print(str(end-st)+" s")