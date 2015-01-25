class Power():
	def __init__(self,amt,growth):
		self.amt = amt
		self.growth = growth

	def grow(self,time):
		for t in range(1,time+1):
			self.amt*=self.growth
		return self.amt

	def shrink(self,time):
		for t in range(1,abs(time)+1):
			


import unittest, random

class TestPower(unittest.TestCase):
	def setUp(self):
		self.g = random.randrange(2,3)
		self.i = random.randrange(2,50)
		print "Original {}, Growth {}".format(self.i, self.g)
	
	def test_grow(self):
		p = Power(self.i,self.g)
		t = random.randrange(1,15)
		print("Time {}".format(t))

		p.grow(t)
		val = self.i*self.g**t
		self.assertEqual(p.amt,val)

if __name__ == '__main__':
	unittest.main()

