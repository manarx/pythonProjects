class Product(object):
	__id = 0

	def __init__(self, name, price, quantity):
		self._name = name
		self._price = price
		self._quantity = quantity
		self.__id = Product.__id
		Product.__id += 1

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
