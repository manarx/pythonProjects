#Collatz Conjecture
#Start with a number n > 1. Find the number of steps it takes to reach one using the following process:
#If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.
import sys

def countSteps(n):
	if n < 1:
		sys.exit('The number is smaller than 1')
	step = 0
	while (n != 1):
		if n % 2 == 0:
			n /= 2
		else:
			n = n*3 + 1
		step += 1
	return step


num = int(raw_input('number: '))
step = countSteps(num)
print 'The number of steps to reach 1 is %s' % step
