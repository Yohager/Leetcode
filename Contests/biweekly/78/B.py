class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0] * n 
        f[0] = nums[0]
        for i in range(1,n):
            f[i] = f[i-1] + nums[i]
        
        ans = 0
        for i in range(n-1):
            if f[i] >= f[-1] - f[i]:
                ans += 1 
        return ans 