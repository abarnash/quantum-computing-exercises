class Matrix():
	def __init__(self,rows):
		self.rows = rows
		self.m = len(rows)
		self.n = len(rows[0])
		self.mrange = range(0,self.m)
		self.nrange = range(0,self.n)

	@classmethod
	def _rows_to_Matrix(rows):
		return Matrix(rows)

	@staticmethod
	def _get_zero_Matrix(m,n):
		zeros = []
		for i in range(0,m-1):
			zeros.append([])
			for j in range(0,n-1):
				zeros[i].append(0)
		return Matrix(zeros)

	def __mul__(self,matrix):
		product = Matrix._get_zero_Matrix(self.n,matrix.m)
		for i in self.mrange:
			for j in matrix.nrange:
				for r in self.nrange:
					product.rows[i][j] += self.rows[i][r] * matrix.rows[r][j]
		return product		

import unittest

class TestMatrix(unittest.TestCase):
	def setUp(self):
		self.a = Matrix([[1,-1,3],[0,4,2]])
		self.b = Matrix([[3,1],[2,-4],[-1,0]])
		self.a_mul_b = [[-2, 5],[6, -16]]

	def test_add(self):
		c = self.a * self.b
		self.assertEqual(c.rows,self.a_mul_b)

if __name__ == '__main__':
	unittest.main()