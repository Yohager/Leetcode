class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        首先考虑当前的状态是否只取决于上一个时刻的状态
        考虑i位置，如果i-1没选，则i可以选也可以不选，如果i-1选了则i不可以选
        '''
        '''
        当然我们还可以考虑另外一种方案
        考虑dp[i]表示为当小偷路过到第i个房间时的最大的收益
        此时考虑可能存在的情况：在第i-1个房间没有选，则在i的最大收益一定为dp[i-2]+nums[i]
        如果在第i-1个房间选了，则在第i个房间的值只能为：dp[i-1]
        二者取高的值即可
        '''
        n = len(nums)
        dp = [[0]* 2 for _ in range(n)] 
        dp[0][0] = 0
        dp[0][1] = nums[0]
        for i in range(1,n):
            # 第一列表示当前pos我抢的收益
            # 第二列表示当前pos我不抢的收益
            dp[i][0] = max(dp[i-1][0],dp[i-1][1])
            dp[i][1] = dp[i-1][0]+nums[i]
        return max(dp[-1])