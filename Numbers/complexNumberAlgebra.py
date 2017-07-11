#Complex Number Algebra
#Show addition, multiplication, negation, and inversion of complex numbers in separate functions.
#(Subtraction and division operations can be made with pairs of these operations.)
#Print the results for each operation tested.
import sys

class ComplexNumber(object):
	def __init__(self, real=0, imaginary=0):
		self.real = real
		self.imaginary = imaginary

	def __str__(self):
		imgPart = '%si' %(self.imaginary) if self.imaginary else '' 
		realPart = '%s' % ( self.real if self.real != 0 else '')
		if self.real != 0 and self.imaginary > 0:
			imgPart = '+'+imgPart
		return '0' if self.real == 0 and self.imaginary ==0  else realPart + imgPart

	def __add__(self, cNum):
		rl = self.real + cNum.real
		imgr = self.imaginary + cNum.imaginary
		return ComplexNumber(rl, imgr)

	def __mul__(self, cNum):
		rl = (self.real * cNum.real) - (self.imaginary * cNum.imaginary)
		imgr = (self.real * cNum.imaginary) + (self.imaginary * cNum.real)
		return ComplexNumber(rl, imgr)

	def __sub__(self, cNum):
		return self + ComplexNumber(-1) * cNum

	def __div__(self, cNum):
		a =  self * ComplexNumber(cNum.real, -cNum.imaginary)
		return a * ComplexNumber(1/float(cNum.real**2 + cNum.imaginary**2))


try:
	print 'Please add real and imaginary parts for the complex numbers'
	c1 = ComplexNumber()
	c1.real = int(raw_input('c1.real: '))
	c1.imaginary = int(raw_input('c1.imaginary: '))
	print 'First complex number is %s' %c1
        c2 = ComplexNumber()
        c2.real = int(raw_input('c2.real: '))
        c2.imaginary = int(raw_input('c2.imaginary: '))
        print 'Second complex number is %s' %c2
	print '(%s) + (%s) = %s' % ( c1, c2, c1+c2)
	print '(%s) - (%s) = %s' % ( c1, c2, c1-c2)
	print '(%s) * (%s) = %s' % ( c1, c2, c1*c2)
	print '(%s)/(%s) = %s' % ( c1, c2, c1/c2)
except:
	sys.exit('Invalid input')

#c1 = ComplexNumber(-2,5)
#c2 = ComplexNumber(-2,-5)
#c3 = ComplexNumber(-2,0)
#c4 = ComplexNumber(2,0)
#c5 = ComplexNumber(0,5)
#c6 = ComplexNumber(0,-5)
#ls = [c, c1, c2, c3, c4, c5, c6]
#for i in ls:
#	print i
#print '(%s) + (%s) = %s' % ( c, c1, c+c1)
#print '(%s) + (%s) = %s' % ( c, c4, c+c4)
#print '(%s) + (%s) = %s' % ( c1, c4, c1+c4)
#print '(%s) + (%s) = %s' % ( c, c5, c+c5)

#print '(%s) x (%s) = %s' % ( c, c1, c*c1)
#print '(%s) x (%s) = %s' % ( c, c4, c*c4)
#print '(%s) x (%s) = %s' % ( c1, c4, c4*c1)
#print '(%s) x (%s) = %s' % ( c, c5, c5*c)
#print '(%s) x (%s) = %s' % ( c1, c2, c1*c2)

#print '___SUBTRACTION___'
#print '(%s) - (%s) = %s' % ( c, c1, c - c1)
#print '(%s) - (%s) = %s' % ( c, c4, c - c4)
#print '(%s) - (%s) = %s' % ( c4, c1, c4 - c1)
#print '(%s) - (%s) = %s' % ( c5, c, c5 - c)
#print '(%s) - (%s) = %s' % ( c1, c2, c1 - c2)

#print '___DIVISIION___'
#print '(%s)/(%s) = %s' % ( c, c1, c/c1)
#print '(%s)/(%s) = %s' % ( c, c4, c/c4)
#print '(%s)/(%s) = %s' % ( c4, c1, c4/c1)
#print '(%s)/(%s) = %s' % ( c5, c, c5/c)
#print '(%s)/(%s) = %s' % ( c1, c2, c1/c2)
