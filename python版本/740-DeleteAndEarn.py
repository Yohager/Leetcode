class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        n = max(nums)
        dp = [0 for _ in range(n+1)]
        for i in range(1,n+1):
            dp[i] = max(dp[i-1],dp[i-2] + i * c[i])
        print(dp)
        return dp[-1]