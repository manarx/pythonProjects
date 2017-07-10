def fibonacci(n):
	n1, n2 = 1, 1
	i = 2
	for i in range(2, n):
		n1, n2 = n2, n1 + n2
	return n2

user_input = raw_input('Enter a number: ')
print fibonacci(int(user_input))
