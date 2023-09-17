# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 21000?

def mod16(power):

	if type(power) != int or power < 0:
		raise ValueError("The dimensions must be integers greater than or equal to zero")

	product = 2 ** power
	sum = 0
	for i in str(product):
		sum += int(i)
	return sum 

print(mod16(10))