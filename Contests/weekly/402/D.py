class Fenwick:
    _slots = 'f'

    def __init__(self, n):
        self.f = [0] * n
    
    def update(self, i, val):
        while i < len(self.f):
            self.f[i] += val 
            i += i & -i 
    def pre(self, i):
        res = 0
        while i > 0:
            res += self.f[i]
            i &= i - 1
        return res 
    def query(self, l ,r):
        if r < l:
            return 0
        return self.pre(r) - self.pre(l - 1)

class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        f = Fenwick(n - 1)
        def update(i, val):
            if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
                f.update(i, val)
        for i in range(1, n - 1):
            update(i, 1)
        
        ans = []
        for operation, i, val in queries:
            if operation == 1:
                ans.append(f.query(i + 1, val - 1))
                continue 
            for j in range(max(i - 1, 1), min(i + 2, n - 1)):
                update(j, -1)
            nums[i] = val 
            for j in range(max(i - 1, 1), min(i + 2, n - 1)):
                update(j, 1)
        return ans
