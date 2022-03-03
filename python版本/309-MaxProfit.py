class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        定义状态: dp[i][j]表示第i天的第j个状态
        dp[i][0]：第i天买入的最大收益
        dp[i][1]：第i天卖出最大的收益
        dp[i][2]：第i天冷冻期的最大收益
        '''
        n = len(prices)
        dp = [[-float('inf')]*3 for _ in range(n)]
        dp[0][0] = -prices[0]
        for i in range(1,n):
            dp[i][0] = max(dp[i-1][0],-prices[i],dp[i-1][2]-prices[i])
            dp[i][1] = max(dp[i-1][1],dp[i-1][0]+prices[i])
            dp[i][2] = max(dp[i-1][1],dp[i-1][2])
        # print(dp)
        return max(dp[-1]) if max(dp[-1]) >= 0 else 0