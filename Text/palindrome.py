"""
Check if Palindrome
Checks if the string entered by the user is a palindrome.
That is that it reads the same forwards as backwards like racecar
"""

text = raw_input('Enter text \n>>> ')
is_palindrome = text == ''.join(text[::-1])
print ['Not a palindrome','Yes, it is a palindrome'][int(is_palindrome)]
