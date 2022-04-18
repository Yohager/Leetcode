from ast import Str
import random 
'''
线段树 (二叉树形数据结构)
存储区间或者线段 快速查询结构内包含某一个的所有区间
一个包含n个区间的线段树 空间复杂度为O(n) 查询时间复杂度为O(log n + k) 其中k是符合条件的区间数量
'''

class ST:
    def __init__(self,nums) -> None:
        self.n = len(nums)
        self.tree = [0] * (2*self.n)
        for i in range(self.n,2*self.n):
            self.tree[i] = nums[i-self.n]
        for i in range(self.n-1,0,-1):
            self.tree[i] = self.tree[2*i] + self.tree[(2*i)|1]
    
    def add(self,i,val):
        # 将原数组下标转换为线段树下标
        i += self.n 
        self.tree[i] = val
        while i > 0:
            self.tree[i//2] = self.tree[i] + self.tree[i^1] 
            i //= 2  
    def RangeSum(self,i,j):
        i += self.n 
        j += self.n 
        total = 0
        while i <= j:
            if i & 1:
                total += self.tree[i]
                i += 1
            if not j & 1:
                total += self.tree[j]
                j -= 1
            i //= 2
            j //= 2
        return total 
    


'''
segment tree with range updating 
模板来自于大佬Minori

'''
class SegmentTree:
    def __init__(self,u,v) -> None:
        self.u, self.v = u, v 
        self.label = 0 
        if u == v:
            self.left, self.right = None, None 
        else:
            self.left = SegmentTree(u,self.mid)
            self.right = SegmentTree(self.mid+1,v)
    
    @property
    def mid(self):
        return (self.u + self.v) // 2
    
    def update(self,t,u,v):
        # t: value, u: lower_bound, v: upper_bound 
        if u <= self.u and self.v <= v:
            self.label = t 
            return 
        if self.label != -1:
            self.left.label = self.label 
            self.right.label = self.label 
            self.label = -1 
        if u <= self.mid:
            self.left.update(t,u,v)
        if self.mid < v:
            self.right.update(t,u,v)
    
    def query(self):
        if self.label != -1:
            return self.label * (self.v - self.u + 1)
        return self.left.query() + self.right.query()
    

'''
线段树每个节点表示为一个区间的信息
root: 1 - n
left: 1 - (n+1)/2 
right: (n+1)/2+1 - n
leaves: 1,2,...,n 

希望求解一个区间: (l,r) 只有左右两端可能两个区间, 中间都可以向上选择区间
希望更改某个位置的值: 更改路径上的所有点的值

1.建树
2.修改值
3.询问
'''
class STree:
    def __init__(self,nums,n) -> None:
        self.nums = nums 
        self.n = n
        self.t = [0] * (4*self.n + 1)

    def BuildTree(self,k,l,r):
        if (l == r):
            self.t[k] = self.nums[l]
            return 
        m = (l+r) >> 1
        self.BuildTree(k+k,l,m)
        self.BuildTree(k+k+1,m+1,r)
        self.t[k] = self.t[k+k] + self.t[k+k+1]
    
    def Add(self,k,l,r,idx,v):
        self.t[k] += v
        if (l == r):
            return 
        m = (l+r) >> 1
        if idx <= m:
            # left tree
            self.Add(k+k,l,m,idx,v)
        else:
            # right tree
            self.Add(k+k+1,m+1,r,idx,v)
    
    def Query(self,k,l,r,s,t):
        # calculate the range sum from s to t 
        if l == s and r == t:
            # 区间完全相等 直接给出这个区间的求和的值
            return self.t[k]
        m = (l+r) >> 1 
        if t <= m:
            # left tree 
            return self.Query(k+k,l,m,s,t)
        else:
            if s > m:
                return self.Query(k+k+1,m+1,r,s,t)
            else:
                # 横跨两个区间
                return self.Query(k+k,l,m,s,m) + self.Query(k+k+1,m+1,r,m+1,t)


# if __name__ == "__main__":
#     nums = [0] + [random.randint(1,100) for _ in range(20)]
#     n = 20
#     print(nums)
#     ST1 = STree(nums,n)
#     ST1.BuildTree(1,1,n)
#     print(ST1.Query(1,1,n,1,n))
#     print(sum(nums))
