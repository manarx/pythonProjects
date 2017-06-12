import weakref
from collections import defaultdict

class Product(object):
	__id = 0
	__instances__ = defaultdict(list)	

	def __init__(self, name, price = 0, quantity = 0):
		self._name = name
		self._price = price
		self._quantity = quantity
		self.__id = Product.__id
		Product.__id += 1
		self.__instances__[self.__class__].append(weakref.ref(self))

	@classmethod
	def get_instances(cls):
		for inst_ref in cls.__instances__[cls]:
			inst = inst_ref()
			if inst is not None:
				print inst

	@staticmethod
	def createNew():
		print 'Please enter the following details:'
		name = raw_input('name: \t')
		quantity = raw_input('quantity: \t')
		while not quantity.isdigit() or int(quantity) < 0:
			print '%s is not a valid qunatity value.'
			quantity = input('quantity: \t')
		quantity = int(quantity)
		price = raw_input('price: \t')
                while not price.isdigit() or int(price) < 0: #TODO: check if the price is type float
                        print '%s is not a valid price value.'
                        price = input('price: \t')
                price = int(price)
		try:
			pr = Product(name, price, quantity)
			print '%s has been created.' %pr.name
		except Exception as e:
			print e.message

	@property
	def name(self):
		return self._name

	@property
	def quantity(self):
		return self._quantity

	@quantity.setter	
	def quantity(self, value):
		if value < 0:
			raise TypeError('Quantity cannot be negative')
		self._quantity = value

	@property
	def price(self):
		return self._price

	@price.setter
	def price(self, value):
		if value < 0:
			raise TypeError('Price cannot be negative')
		self._price = value

	def __str__(self):
		return 'Product name:\t %s\n quantity:\t %s\n  price:\t %s'%(self.name, self.quantity, self.price)


#Product.createNew()
#Product.get_instances()
