from Complex import Complex
import itertools


class Vector():
	def __init__(self,*c):
		self.data = []
		for i in c:
			self.data.append(c)

class ComplexVector(Vector):
	def __init__(self,*c):
		self.data = []
		self.cur = 0
		self.type = 'ComplexVector'
		for i in c:
			self.data.append(Complex(i[0],i[1]))

	def __len__(self):
		return len(self.data)

	def __iter__(self):
		return self

	def next(self): # Python 3: def __next__(self)
		if self.cur > len(self.data):
			raise StopIteration
		else:
			self.cur += 1
			return self.data[self.cur - 1]

	def _append_out(self,cvect,op):
		if len(cvect) == len(self.data):
			vect = []
			for i,i2 in itertools.izip(self.data,cvect):
				vect.append(getattr(i,op)(i2))
			return ComplexVector(vect)
		else:
			raise ValueError("Vectors have different dimensions")

	def __add__(self,cvect):
		return self._append_out(cvect,'__add__')

	def __sub__(self,cvect):
		return self.append_out(cvect,'__sub__')

	def scalar_multiply(obj):
		prod = []
		for i in self.data:
			val = i * obj
			prod.append(val)
		return ComplexVector(*prod)

	def vector_multiply(self,obj):
		return self._append_out(obj,'__mul__')

	def __mul__(self,obj):
		print(type(obj))
		if obj.type in ['Complex','int','float','long']:
			if obj in ['int','float','long']:
				obj = Complex(obj,0)
			self.scalar_multiply(obj)
		elif obj.type == 'ComplexVector':
			self.vector_multiply(obj)
		else:
			raise ValueError('Invalid argument for multiplication')

	def inverse(self):
		inverse = []
		for i in self.data:
			inverse.append(Complex(0,0) - i)
		return ComplexVector(inverse)

	def inner_product(self,cvect):
		return

	def normalize(self):
		return

	def distance(self):
		return

class ComplexMatrix():
	def __init__(self,vals):
		self.data = vals
		self.m = len(vals)
		self.n = len(vals[0])
		self.index = [0,0]
		self.type = "ComplexMatrix"

	def __iter__(self):
		return self

	def next(self): # Python 3: def __next__(self)
		if self.index[1] >= self.n
			raise StopIteration
		else:
			if self.index[1] >= self.m:
				self.index[0] += 1
				self.index[1] = 0
			return self.data[self.index[0],self.index[1]]
	
	def __add__(self,matrix):
		mat = []
		for i in self.m-1:
			row = []
			for j in self.n-1:
				s = self.data[j][i] + matrix[i][j]
				row.append(s)
			mat.append(row)
		return ComplexMatrix(mat)

	def loop_through(self):
		for i in self.m-1:
			for j in self.n-1:
				yield self.data[i][j]

	def inverse(self):
		mat = []
		for i in self.m-1:
			row = []
			for j in self.n-1:
				s = self.data[i][j].inverse()
				row.append(s)
			mat.append(row)
		return ComplexMatrix(mat)

	def scalar_multiply(obj):
		prod = []
		for i in self.data:
			val = i * obj
			prod.append(val)
		return ComplexVector(*prod)

	def vector_multiply(self,obj):
		obj = ComplexMatrix(obj)
		return 

	def matrix_multiply(self,obj):
		mat = []
		for i in range(0,self.m-1):
			row = []
			r = self.data[i]
			for oi in range(0,obj.n-1):
				c = [obj[oi][oj] for oj in range(0,obj.m-1)]
				s = 0
				for ri,ci in itertools.izip(r,c):
					s += ri*ci
				row.append(s)
			mat.append(row)
		return ComplexMatrix(mat)

	def __mul__(self,obj):
		print(type(obj))
		if obj.type in ['Complex','int','float','long']:
			if obj in ['int','float','long']:
				obj = Complex(obj,0)
			self.scalar_multiply(obj)
		elif obj.type == 'ComplexVector':
			self.vector_multiply(obj)
		elif obj.type == 'ComplexMatrix':
			self.matrix_multiply
		else:
			raise ValueError('Invalid argument for multiplication')


class VectorSpace():
	def __init__(self):
		pass

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
			for r in range(0,10):
				self.cnums.append(self._get_random_cnum())
			return

		def test_init(self):
			c = self.cnums
			v = ComplexVector(c[0],c[1],c[2])
			v2 = ComplexVector(c[3],c[4],c[5])
			v3 = v + v2
			print v3
			print len(v3)
			v4 = v * v3
			print v3.data[0].r, len(v2)	
			print v4.data[0].r	
			return

		def test_add(self):
			return
	unittest.main()