import math


class Complex():
	def __init__(self,r,i):
		self.r = r
		self.i = i
		self.__class__ == 'Complex'

	def _ol_to_comp(self,cnum):
		return Complex(cnum[0],cnum[1])

	def __neg__(self):
		return Complex(self.r,-self.i)

	def __add__(self,cnum):
		"""implements addition operator"""
		cnum = self._ol_to_comp(cnum)
		r = self.r + cnum.r
		i = self.i + cnum.i
		return Complex(r,i)

	def __sub__(self,cnum):
		"""implements subtraction operator"""
		cnum = self._ol_to_comp(cnum)
		r = self.r - cnum.r
		i = self.i - cnum.i
		return Complex(r,i)

	def __mul__(self,cnum):
		"""implements multiplication operator"""
		cnum = self._ol_to_comp(cnum)
		r,i = self.r, self.i
		r2 = r * cnum.r -(i * cnum.i)
		i2 = r * cnum.i + i * cnum.r
		return Complex(r2,i2)

	def __div__(self,cnum):
		r,i = self.r, self.i
		cnum = self._ol_to_comp(cnum)
		cr,ci = cnum.r,cnum.i
		cmod_sq = cnum.modulus_sq()
		r2 = (r*cr + i*ci)/cmod_sq
		i2 = (cr*i - r*ci)/cmod_sq
		return Complex(r2,i2)

	def __eq__(self,cnum):
		cnum = self._ol_to_comp(cnum)
		if not self.r == cnum.r or not self.i == cnum.i:
			return False
		else:
			return True

	def __getitem__(self,index):
		"""implements indexing"""
		if index == 1:
			return self.i
		elif not index:
			return self.r
		else:
			raise IndexError
	def _get_sign(self):
		if self.i <0:
			sign = '-'
		else:
			sign = '+'
		return sign
	def __str__(self):
		sign = self._get_sign()
		return '{} {} {}i'.format(self.r,sign,abs(self.i))

	def __repr__(self):
		sign = self._get_sign()
		return '{} {} {}i'.format(self.r,sign,abs(self.i))

	def modulus_sq(self):
		return self.r**2 + self.i**2

	def modulus(self):
		return math.sqrt(self.modulus_sq())

	def polar(self):
		self.rho = self.modulus()
		self.theta = math.arctan(self.i/self.r)
		return (self.rho,self.theta)


if __name__ == '__main__':
	import unittest
	import random

	class TestComplex(unittest.TestCase):

		def _get_random_cnum(self,low=-10,high=10):
			r = random.randrange(low,high)
			i = random.randrange(low,high)
			return Complex(r,i)

		def setUp(self):
			self.cnums = []
			for r in range(0,3):
				self.cnums.append(self._get_random_cnum())
			return

		def test_neg(self):
			a = self.cnums[0]
			self.assertEqual(-a,Complex(a.r,-a.i))

		def test_add(self):
			a = self.cnums[0]
			b = self.cnums[1]
			c = a + b
			self.assertEqual(c.r, a.r + b.r )
			self.assertEqual(c.i, a.i + b.i)

		def test_sub(self):
			a,b = self.cnums[0],self.cnums[1]
			c = a - b
			self.assertEqual(c.r,a.r - b.r)
			self.assertEqual(c.i,a.i - b.i)

		def test_mul(self):
			a,b = self.cnums[0],self.cnums[1]
			c = a * b
			self.assertEqual(c.r,a.r*b.r-(a.i*b.i))
			self.assertEqual(c.i,a.i*b.r+a.r*b.i)

		def test_div(self):
			a = Complex(-2,1)
			b = Complex(1,2)
			c = Complex(0,1)
			self.assertEqual(a/b,c)

		def test_getitem(self):
			a = self.cnums[0]
			self.assertEqual(a[0],a.r)
			self.assertEqual(a[1],a.i)

		def test_commutative(self):
			a,b = self.cnums[0],self.cnums[1]
			s1 = a + b
			s2 = b + a 
			self.assertEqual(s1,s2)

		def test_associative(self):
			print self.cnums
			a,b,c = self.cnums[0],self.cnums[1],self.cnums[2]
			a1 = (a + b) + c
			a2 = a + (b + c)
			a3 = (a*b)*c
			a4 = a*(b*c)
			self.assertEqual(a1,a2)
			self.assertEqual(a3,a4)

		def test_distributive(self):
			a,b,c = self.cnums[0],self.cnums[1],self.cnums[2]
			d1 = a*(b + c)
			d2 = (a*b) + (a * c)
			self.assertEqual(d1,d2)

		def test_modulus_sq(self):
			a = self.cnums[0]
			self.assertEqual(a.modulus(),math.sqrt(a.modulus_sq()))


	unittest.main()
	