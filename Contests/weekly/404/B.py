class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        k = 2
        dp = [[0] * k for _ in range(k)]
        new_nums = [x % k for x in nums]
        for x in new_nums:
            for j in range(k):
                dp[x][j] = dp[j][x] + 1
        # print(dp)
        return max(map(max, dp))
