class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        '''
        最直觉上的dp应该是dp[i]表示为构成使用coins构成i的种类数量
        '''
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for i in range(c,amount+1):
                dp[i] += dp[i-c]
        return dp[amount]