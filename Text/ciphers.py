#Vigenere / Vernam / Ceasar Ciphers
#Functions for encrypting and decrypting data messages.
import sys

def ceasarCipher(text, shift):
	encodedText = ''.join([chr((ord(i)%65+shift)%26 + 65) if i.isalpha() else i for i in text])
	return encodedText


def vigenereCipher(text, keyword):
	encodedText = ''
	n = 0
	for i in range(len(text)):
		if text[i].isalpha():
			shift = ord(keyword[n%len(keyword)]) % 65
			letter = ceasarCipher(text[i], shift)
			n += 1
		else:
			letter = text[i]
		encodedText += letter
	return encodedText


def vernamCipher(text, keyword):
#	res = map(bin, [ord(text[i]) ^ ord(keyword[i]) for i in range(len(text))])
	encodedText = ''.join([chr(ord(text[i]) ^ ord(keyword[i])) for i in range(len(text))])
	return encodedText

try:
	print 'All letters will be capitalized.'
	print 'Please choose a cipher method:'
	print '\t1 - Ceasar\n\t2 - Vigenere\n\t3 - Vernam'
	choice = int(raw_input('>>> '))
	print('Please enter a text to encrpyt:')
	lines = []
	while True:
		line = raw_input()
		if line:
			lines.append(line)
		else:
			break
	text = ('\n'.join(lines))
	print 'Your text is: \n%s' % text
	if choice == 1:
		shift = int(raw_input('Please enter a number to shift. Add a negative number to shift to the left: '))
		encodedText = ceasarCipher(text.upper(), shift)
		print encodedText
	elif choice == 2:
		keyword = raw_input('Please enter a keyword: ').upper()
		print 'your keyword is %s' %keyword
                encodedText = vigenereCipher(text.upper(), keyword)
                print encodedText
	elif choice == 3:
		keyword = raw_input('Please enter a keyword: ').upper()
                print 'your keyword is %s' %keyword
                encodedText = vernamCipher(text, keyword)
                print encodedText
	else:
		Exception('invalid input')
		

except:
	sys.exit('Invalid input')
