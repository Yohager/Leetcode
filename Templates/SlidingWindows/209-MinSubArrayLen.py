class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0,0
        ans = float('inf') # 定义需要维护的值
        total = 0 # 定义需要维护的值
        while l < n and r < n:
            total += nums[r]
            if total >= target:
                ans = min(ans,r-l+1)
            
            while total >= target:
                ans = min(ans,r-l+1)
                total -= nums[l]
                l += 1
            r += 1
        return ans if ans != float('inf') else 0