from fractions import Fraction

def add(a, b):
	print 'Result of Addition: {0}'.format(a+b)
def subtract(a, b):
	print 'Result of Subtraction: {0}'.format(a-b)
def divide(a, b):
	print 'Result of Division: {0}'.format(a/b)
def multiply(a, b):
	print 'Result of Multiplication: {0}'.format(a*b)

while True:
	a = Fraction(raw_input("Enter first fraction: "))
	b = Fraction(raw_input("Enter second fraction: "))
	op = raw_input('Operation to perform - Add, Subtract, Divide, Multiply: ')
	if op == 'Add':
		add(a, b)
	elif op == 'Subtract':
		subtract(a, b)
	elif op == 'Divide':
		divide(a, b)
	elif op == 'Multiply':
		multiply(a, b)
	answer = raw_input('Do you want to exit? (y) for yes ')
	if answer == 'y':
		break