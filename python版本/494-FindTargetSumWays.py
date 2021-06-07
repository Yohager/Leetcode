class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if sum(nums) < target or (sum(nums)-target) % 2:
            return 0
        rm = (sum(nums)-target) // 2
        dp = [1] + [0] * rm 
        for i in nums:
            for j in range(rm,-1,-1):
                if j >= i:
                    dp[j] = dp[j] + dp[j-i]
        #print(dp)
        return dp[-1]
