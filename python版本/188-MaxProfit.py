class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if prices == []:
            return 0

        n = len(prices)
        k = min(k,n//2)
        buy = [[0 for _ in range(k+1)] for _ in range(n)]
        sell = [[0 for _ in range(k+1)] for _ in range(n)]
        
        buy[0][0], sell[0][0] = -prices[0], 0

        for x in range(1,k+1):
            buy[0][x] = sell[0][x] = float("-inf")

        for i in range(1,n):
            buy[i][0] = max(buy[i-1][0],sell[i-1][0]-prices[i])
            for j in range(1,k+1):
                buy[i][j] = max(buy[i-1][j],sell[i-1][j] - prices[i])
                sell[i][j] = max(sell[i-1][j],buy[i-1][j-1] + prices[i])
        
        return max(sell[n-1])