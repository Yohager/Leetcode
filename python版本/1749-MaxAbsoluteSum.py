class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return abs(nums[0])
        n = len(nums)
        '''
        使用dp的话
        dp[i] = max(dp[i-1]+nums[i],nums[i])
        '''
        sums = []
        cur = 0
        for i in range(n):
            cur += nums[i]
            sums.append(cur)
        sums.sort()
        ans = abs(sums[n-1]-sums[0])
        for i in range(len(sums)):
            m = abs(sums[i])
            if m > ans:
                ans = m
        return ans