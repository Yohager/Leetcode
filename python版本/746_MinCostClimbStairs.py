class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        dp = [0]*(len(cost))
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2,len(dp)):
            dp[i] = min(dp[i-2]+cost[i],dp[i-2]+dp[i-1]+cost[i],dp[i-1]+cost[i])
        return dp[-1]