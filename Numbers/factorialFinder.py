#Factorial Finder
#The Factorial of a positive integer, n, is defined as the product of the sequence
# n, n-1, n-2, ...1 and the factorial of zero, 0, is defined as being 1.
#Solve this using both loops and recursion.
import sys

#recursion
#NOTE: The recursion depth is 999. So any number bigger than 1000 will result in an error with this method
def factorial(n):
	if n <= 2:
		return n
	else:
		return n*factorial(n-1)

#iteration
def factorialIterative(n):
	f = 1
	while n >= 2:
		f *= n
		n -= 1
	return f
		
num = int(raw_input('Please enter a number:' ))
print 'The factorial of %s with iterative method is %s' %(num, factorialIterative(num))
if num > 1000:
	sys.exit('%s exceeds the recursive depth.' %num)
print 'The factorial of %s with recursive method is %s'%( num, factorial(num))

