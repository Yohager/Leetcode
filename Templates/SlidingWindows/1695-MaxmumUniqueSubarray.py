class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans = 0 # 维护变量
        l,r = 0,0
        n = len(nums)
        total = 0 # 维护变量
        s = {} # 维护变量
        while l < n and r < n:
            total += nums[r]
            s[nums[r]] = s.get(nums[r],0) + 1
            if len(s) == r - l + 1:
                ans = max(total,ans)
            
            while len(s) < r - l + 1:
                total -= nums[l]
                s[nums[l]] -= 1
                if s[nums[l]] == 0:
                    s.pop(nums[l])
                l += 1
            r += 1
        return ans 