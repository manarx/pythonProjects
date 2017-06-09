"""
Count Vowels
Enter a string and the program counts the number of vowels in the text.
For added complexity have it report a sum of each vowel found.
"""

text = raw_input('enter some text \n>>> ')
vowels = ['a','e','o','u','i']

eachVowelSum = {i: text.count(i) for i in vowels if text.count(i) != 0} 

sumOfVowels = sum([eachVowelSum[i] for i in eachVowelSum.keys()])

print eachVowelSum

print 'sum of all vowels: ' + str(sumOfVowels)
