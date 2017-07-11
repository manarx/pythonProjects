#Credit Card Validator
#Takes in a credit card number from a common credit card vendor
#(Visa, MasterCard, American Express, Discoverer) and validates it 
#to make sure that it is a valid number

#This method uses Luhn Algorithm
# https://en.wikipedia.org/wiki/Luhn_algorithm
def validate(number):
#	ls = map(int, str(number)[::-1]))
	sumi, n = 0, 0
	ls = map(int, number[::-1])
	for i in range(len(ls)):
		if i%2==0:
			sumi += ls[i]
		else:
			n = ls[i]*2
			if n>9:
				n = sum(map(int,str(n)))
			sumi += n
	return sumi % 10 == 0

ccNum = raw_input('Please enter a credit card number to validate: ')
print 'This is a valid credit card' if validate(ccNum) else 'It is not valid'
	
