class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        偷窃到第i个房子的最大的金额dp[i]
        dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        '''
        n = len(nums)
        if n <= 2:
            return max(nums)
        dp = [0] * n 
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,n):
            dp[i] = max(dp[i-1],nums[i]+dp[i-2])
        return dp[-1]