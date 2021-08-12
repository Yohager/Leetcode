class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n+1)]
        res = 0

        for i in range(n):
            for j in range(i):
                d = nums[i] - nums[j]
                # 更新 i 下面的 hashmap
                dp[i][d] += dp[j][d] + 1
                # 前一个结果作为数组下标 i 可以组成的等差数列数组个数
                res += dp[j][d]
        return res 