class BIT:
	def __init__(self, n):
		self.tree = [0] * n 

	def add(self, i, val):
		while i < len(self.tree):
			self.tree[i] += val 
			i += (i & (-i))

	def query(self, i):
		res = 0 
		while i > 0:
			res += self.tree[i]
			i &= i - 1
		return res 