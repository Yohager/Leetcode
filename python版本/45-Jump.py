class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0 
        l,r = 1,1
        for i in range(1,n+1):
            cur = 0
            for j in range(l,r+1):
                cur = max(cur,j+nums[j-1])
            if cur >= n:
                return i 
            l = r + 1
            r = cur 
        return n 
