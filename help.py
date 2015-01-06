import sys
import math
def factorial(n):
	'''This is a docstring test.

	>>> factorial(100)
	93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000L
	'''
	#if factorial(n) == factorial(n-1):
	#	raise ValueError('Calculated value of factorial is too large.')

	if n in [0,1]:
		n == n

	elif n > 1:
		n = n * factorial(n-1)

	elif n < 0:
		raise ValueError('Factorial is not defined for negative numbers.')

	return n

def factorial_loop(n):
	'''This is a docstring test.

	>>> factorial_loop(100)
	93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000L
	'''
	answer = 1
	for i in range(n):
		answer = answer * (i + 1)

	return answer

if __name__ == "__main__":
    import doctest
    doctest.testmod()

import unittest

class TestFactorialTime(unittest.TestCase):

	def setUp(self):
		self.n = 100

	def test_factorial_time(self):
		self.AssertEqual(factorial(self.n,self.n))


suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
unittest.TextTestRunner(verbosity=2).run(suite)
