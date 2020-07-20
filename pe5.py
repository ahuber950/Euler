#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#define function for listing primary factors
import math
import time
st=time.time()

def pfacs(num):
	primes = []
	for i in range(2,num+1):
		while num%i==0:
			primes.append(i)
			num/=i
		if num==1:
			break
	return primes

def prod(list):
	p=1
	for i in list:
		p*=i
	return p

x=int(input("I want the smallest number that is evenly divisible by all numbers from 1 to __\n"))
min_facs = []
for i in range(2,x+1):
	facs_facs = pfacs(i)
	for j in facs_facs:
		while facs_facs.count(j)>min_facs.count(j):
			min_facs.append(j)
			min_facs.sort()
			print(str(min_facs)+" appended "+str(j)+" on i "+str(i))

print(min_facs)
p=prod(min_facs)
print(p)

end=time.time()
print(str(end-st)+" s")