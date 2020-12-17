class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        '''
        做dp首先考虑可能存在的状态：这个题目一种是当天是手里没有股票的状态，第二种是当天是手里持有股票的状态
        第二个问题，分这两种状态考虑对应情况下的最大收益
        1. 手里没有股票：要么前一天就没有，要么前一天还有按照今天的价格卖出了
            这两种情况下对应的最大收益为max{rev1[i-1],rev2[i-1]+price[i]-fee}
        2.手里有股票的情况下，要么前一天延续过来的，要么就是今天买了新的
            这两种情况下对应的最大收益为max{rev2[i-1],rev1[i-1]-price[i]}
        '''
        dp1 = [0] * len(prices)
        dp2 = [0] * len(prices)
        dp1[0] = 0
        dp2[0] = -prices[0]
        for i in range(1,len(prices)):
            dp1[i] = max(dp1[i-1],dp2[i-1]+prices[i]-fee)
            dp2[i] = max(dp2[i-1],dp1[i-1]-prices[i])
        return dp1[-1]