# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
# contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British usage.

wholes = {
	"0": 0,
	"1": 3,
	"2": 3,
	"3": 5,
	"4": 4,
	"5": 4,
	"6": 3,
	"7": 5,
	"8": 5,
	"9": 4
}

tens = {
	"0": 0,
	"2": 6,
	"3": 6,
	"4": 5,
	"5": 5,
	"6": 5,
	"7": 7,
	"8": 6,
	"9": 6
}

teens = {
	"0": 3,
	"1": 6,
	"2": 6,
	"3": 8,
	"4": 8,
	"5": 7,
	"6": 7,
	"7": 9,
	"8": 8,
	"9": 8
}
def letter_count(num):

	if type(num) != int or num < 1:
		raise ValueError("The number must be an integer greater than zero")

	sum = 0
	num = str(num)

	if len(num) == 1:
		sum += wholes[num[0]]
	if len(num) > 1:
		if num[-2] == "1":
			sum += teens[num[-1]]
		else:
			sum = sum + tens[num[-2]]
			sum += wholes[num[-1]]
	if len(num) > 2 and num[-3] != "0":
		sum = sum + 7 + wholes[num[-3]]
		if num[-1] != "0" or num[-2] != "0":
			sum += 3
	if len(num) == 4:
		sum = sum + 8 + wholes[num[-4]]
	return sum

def mod17(maxnum):

	if type(maxnum) != int or maxnum < 1:
		raise ValueError("The maxnumber must be an integer greater than zero")

	sum = 0
	for i in range(1,maxnum + 1):
		sum += letter_count(i)
	return sum

print(mod17(1000))