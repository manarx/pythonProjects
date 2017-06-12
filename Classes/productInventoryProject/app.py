from Product import Product
from Inventory import Inventory

def main():
	print 'Welcome'
	intro = """
	Please choose one of the following options:
	1. View inventory
	2. View all available products
	3. Add a new product
	4. Exit

	>>> """
	viewInventory = '1'
	viewAllProducts = 'Product.get_instances()'
	createNewProduct = 'Product.createNew()'
	exit = 'quit()'	
	options = [viewInventory, viewAllProducts, createNewProduct, exit]

	while True:
		try:
			choice = raw_input(intro)
			while choice not in map(str, range(1, 6)):
				#raise TypeError('Not a valid option')
				print '\t%s is not a valid option' %choice
				choice = raw_input(intro)
			choice = int(choice)
			print 'Integer: %s' %choice
		except Exception as e:
			print e.message
	
		exec(options[choice-1])


if __name__ == '__main__':
	main()		
