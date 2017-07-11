#Vigenere / Vernam / Ceasar Ciphers
#Functions for encrypting and decrypting data messages.
import sys

def ceasarCipher(text, shift):
	encodedText = ''.join([chr(97+(((ord(i)+shift)%97)%26)) if i.islower() else chr(65+(((ord(i)+shift)%65)%26)) if i.islower() else i for i in text])
	return encodedText





try:
	print 'Please choose a cipher method:'
	print '\t1 - Ceasar\n\t2 - Vigenere\n\t3 - Vernam'
	choice = int(raw_input('>>> '))
	print('Please enter a text to encrpyt. To end enter "END" in a new line')
	lines = []
	while True:
		line = raw_input()
		if line:
			lines.append(line)
		else:
			break
	text = '\n'.join(lines)
	print 'Your text is: \n%s' % text
	if choice == 1:
		shift = int(raw_input('Please enter a number to shift. Add a negative number to shift to the left: '))
		encodedText = ceasarCipher(text, shift)
		print encodedText

except:
	sys.exit('Invalid input')
