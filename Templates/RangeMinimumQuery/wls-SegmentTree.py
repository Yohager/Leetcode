'''
来自于wls的线段树的模板
'''
'''
part one 
1. 建树
2. 更新单点值
3. 区间查询

更新与查询时间复杂度为O(log n)
'''
class SegmentTree(object):
	"""docstring for SegmentTree"""
	def __init__(self, nums):
		super(SegmentTree, self).__init__()
		self.nums = nums 
		self.n = len(self.nums)
		self.t = [0] * (4*n+1)

	def BuildTree(self,k,l,r):
		# k表示在线段树中的下标, l,r 分别表示区间的端点
		if l == r:
			self.t[k] = self.nums[l]
			return 
		m = (l+r) >> 1
		self.BuildTree(k+k,l,m)
		self.BuildTree(k+k+1,m+1,r)
		self.t[k] = self.t[k+k] + self.t[k+k+1]

	def UpdateValue(self,k,l,r,idx,v):
		# k表示线段树位置下标，l,r分别表示区间端点，idx表示原数组中的位置，v表示需要更新出来的值
		self.t[k] += v 
		if (l == r):
			return 
		m = (l+r) >> 1
		if x <= m:
			# 向左边递归
			self.UpdateValue(k+k,l,m,idx,v)
		else:
			self.UpdateValue(k+k+1,m+1,r,idx,v)

	def QueryRange(self,k,l,r,s,t):
		# k表示在线段树位置的下标，l,r表示区间端点, s,t表示为需要问询的区间的端点
		if (l == s) and (r == t):
			return self.t[k]
		m = (l+r) >> 1
		if t <= m:
			return self.QueryRange(k+k,l,m,s,t)
		else:
			if s > m:
				return self.QueryRange(k+k+1,m+1,r,s,t)
			else:
				return self.QueryRange(k+k,l,m,s,m) + self.QueryRange(k+k+1,m+1,r,m+1,t)


'''
part two 
支持区间修改以及区间查询
log n的区间修改，我们需要使用一个新的变量v用于进行标记
log n的区间查询，考虑一个区间的查询，分为两个部分上面的v的部分以及下面整体的部分
'''
class SegmentTree2(object):
	"""docstring for SegmentTree2"""
	def __init__(self, nums):
		super(SegmentTree2, self).__init__()
		self.nums = nums 
		self.n = len(self.nums) - 1
		self.t = [0] * (4*self.n+1)
		self.v = [0] * (4*self.n+1) #self.v[k]表示当前k位置的区间每个值都需要更新的值

	def BuildTree(self,k,l,r):
		# the same as the last class 
		if (l == r):
			self.t[k] = self.nums[l]
			return 
		m = (l+r) // 2
		self.BuildTree(k+k,l,m)
		self.BuildTree(k+k+1,m+1,r)
		self.t[k] = self.t[k+k] + self.t[k+k+1]

	def UpdateRange(self,k,l,r,x,y,z):
		# 在x到y的区间更新为z
		if (l == x) and (r == y):
			self.v[k] += z 
			return 
		self.t[k] += (y-x+1) * z 
		m = (l+r) >> 1 
		if y <= m:
			self.UpdateRange(k+k,l,m,x,y,z)
		else:
			if (x > m):
				self.UpdateRange(k+k+1,m+1,r,x,y,z)
			else:
				self.UpdateRange(k+k,l,m,x,m,z)
				self.UpdateRange(k+k+1,m+1,r,m+1,y,z)

	def QueryRange(self,k,l,r,s,t,p):
		# 问询s到t的区间的值
		# p表示为走到当前的点v的值累计和为多少
		p += self.v[k]
		if (l == s) and (r == t):
			return self.t[k] + (r-l+1) * p 
		m = (l+r) >> 1
		if t <= m:
			return self.QueryRange(k+k,l,m,s,t,p)
		else:
			if s > m:
				return self.QueryRange(k+k+1,m+1,r,s,t,p)
			else:
				return self.QueryRange(k+k,l,m,s,m,p) + self.QueryRange(k+k+1,m+1,r,m+1,t,p)


if __name__ == "__main__":
	n,m = list(map(int,input().split()))
	nums = [0] + list(map(int,input().split()))
	st = SegmentTree2(nums)
	n = len(nums) - 1
	st.BuildTree(1,1,n)
	qs = []
	for i in range(m):
		cur = list(map(int,input().split()))
		qs.append(cur)
	for cur in qs:
		if cur[0] == 1:
			# 更新操作
			st.UpdateRange(1,1,n,cur[1],cur[2],cur[3])
		elif cur[0] == 2:
			# 查询操作
			print(st.QueryRange(1,1,n,cur[1],cur[2],0))

