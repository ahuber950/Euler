#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

x=int(input("For which number do you want the largest prime factor?\n"))

import math
max=math.ceil(math.sqrt(x))
for i in range(2,max):
	while x%i == 0:
		x=x/i
		print(str(i)+" "+str(x))
print(x)
