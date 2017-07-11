#Fibonacci Sequence
#Enter a number and have the program generate the Fibonacci
#sequence to that number or to the Nth number.

def printFibonacci(n):
	n1, n2 = 1, 1
	i = 2
	print n1, n2, 
	for i in range(2, n):
		n1, n2 = n2, n1 + n2
		print n2,

user_input = raw_input('Enter a number: ')
printFibonacci(int(user_input))
