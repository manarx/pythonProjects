from Product import Product

class Inventory(object):

        def __init__(self, products):
                self._products = products

	@property
	def products(self):
		return self._products

	@products.setter
	def products(self, values):
#		if isinstance(values, list):
#			raise TypeError('A list of products is needed.')
		for value in values:
			if not isinstance(value, Product):
				raise TypeError('A type Product is needed')
		self._products = values

        def add_product(self, product):
		self.products = self.products + [product]

	@property
        def value(self):
                return sum([i.price for i in self.products])
"""
apple = Product('apple', 3,3)
banana = Product('banana', 4,4)

print 'Products:'
print apple
print banana
bazaar = Inventory([apple, banana])
print 'value at the start is: %s'  %(bazaar.value)
grape = Product('grape',5,5)
bazaar.add_product(grape)
print 'value after adding grape is: %s' %(bazaar.value)
"""
