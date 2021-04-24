class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if target < min(nums):
            return 0
        dp = [0] * (target+1)
        dp[0] = 1
        '''
        这个问题最精髓的dp在于
        对于数字i，dp[i] = dp[i-nums[0]]+dp[i-nums[1]]+...+dp[i-nums[k]]
        只要i > nums[k]就在这个dp上做累加值
        '''
        for i in range(1,target+1):
            for j in nums:
                if i >= j:
                    dp[i] += dp[i-j]
        #print(dp)
        return dp[target]