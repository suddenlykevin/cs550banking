''' inspired by: 
	http://anandology.com/python-practice-book/object_oriented_programming.html
	
	other resources:
	https://docs.python.org/3/reference/datamodel.html
	https://docs.python.org/3/library/operator.html
'''

class RationalNumber:
	def __init__(self, n, d):
		self.n = n
		self.d = d

	def __add__(self, other):
		n = self.n*other.d + self.d*other.n
		d = self.d*other.d
		return RationalNumber(n, d)

	def __sub__(self, other):
		n = self.n*other.d - self.d*other.n
		d = self.d*other.d
		return RationalNumber(n, d)

	def __mul__(self, other):
		n = self.n*other.n
		d = self.d*other.d
		return RationalNumber(n, d)

	def __truediv__(self, other):
		n = self.n*other.d
		d = self.d*other.n
		return RationalNumber(n, d)

	# returns in the string in the form of n/d
	def __str__(self):
		return str(self.n)+"/"+str(self.d) 

	__repr__ = __str__ # returns a printable representation of an object. In this case, we are "anulling" the function so that both str and repr return the same value.

def gcd(a,b):
	while b:
		a, b = b, a%b
	return a

def lcd(a,b):
	return a*b//lcd(a,b)

def main():
	a = RationalNumber(1, 2)
	b = RationalNumber(1, 3)
	# a.d, b.d = lcd(a.d,b.d),lcd(a.d,b.d)
	print(a) # 1/2
	print(b) # 1/3
	print(a+b) # 5/6
	print(a-b) # 1/6
	print(a*b) # 1/6
	print(a/b) # 3/2

main()