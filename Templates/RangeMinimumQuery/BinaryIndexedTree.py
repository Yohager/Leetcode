'''
树状数组 BinaryIndexedTree 或者说叫 Fenwick Tree
多用于高效计算数列的前缀和或者区间和
O(log n)的时间复杂度得到任意前缀和
支持O(log n)的时间内动态修改单点值
空间复杂度为 O(n)
'''
class BIT:
    def __init__(self,n) -> None:
        self.tree = [0] * (n+1)
    
    def lowbit(self,x):
        return x & (-x)
    
    def add(self,i,delta):
        i += 1
        while i < len(self.tree):
            self.tree[i] += delta 
            i += self.lowbit(i)
        
    def Prefix(self,i):
        i += 1
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= self.lowbit(i)
        return total 