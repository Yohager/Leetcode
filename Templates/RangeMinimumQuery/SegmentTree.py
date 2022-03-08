'''
线段树 (二叉树形数据结构)
存储区间或者线段 快速查询结构内包含某一个的所有区间
一个包含n个区间的线段树 空间复杂度为O(n) 查询时间复杂度为O(log n + k) 其中k是符合条件的区间数量
'''
class ST:
    def __init__(self,n) -> None:
        self.n = n 
        self.tree = [0] * (2*n)
    
    def add(self,i,delta):
        # 将原数组下标转换为线段树下标
        i += self.n 
        while i> 0:
            self.tree[i] += delta 
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