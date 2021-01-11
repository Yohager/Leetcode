class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        对于这个题目而言我们进行如下的分析，因为之前做过一道比这个更加复杂的问题
        考虑
        buy[i][j] 表示从[0,i]这些天中进行了j场交易下且持有一只股票的最大收益
        sell[i][j]表示从[0,i]这些天中进行了j场交易且不持有一只股票的最大收益
        对于buy[i][j]来说状态转移的过程我们可以写为：
        buy[i][j]  = max(buy[i-1][j],sell[i-1][j]-price[i])
        解释：在第i天的时候持有一只股票存在两种情况，要么是前一天就持有一只股票；要么是前一天没有股票第i天买了一只股票
        sell[i][j] = max(sell[i-1][j],buy[i-1][j-1]+price[i])
        然后主要的问题就是考虑一些边界的情况
        '''
        n = len(prices)
        buy = [[0 for _ in range(3)] for _ in range(n)]
        sell = [[0 for _ in range(3)] for _ in range(n)]
        buy[0][0] = -prices[0]
        for i in range(1,3):
            buy[0][i] = sell[0][i] = float("-inf")
        
        for j in range(1,n):
            buy[j][0] = max(buy[j-1][0],sell[j-1][0] - prices[j])
            for k in range(1,3):
                buy[j][k] = max(buy[j-1][k],sell[j-1][k] - prices[j])
                sell[j][k] = max(sell[j-1][k],buy[j-1][k-1] + prices[j])
        #print(sell)
        return max(sell[-1])

