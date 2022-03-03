class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        '''
        定义状态：dp[i][j]表示第i个pos下的第j个状态
        dp[i][0]表示到i为止差值为负的状态下最长子序列的长度
        dp[i][1]表示到i为止差值为正的状态下最长子序列的长度
        状态的转移：
        dp[i][0] = dp[i-1][0] 或者 dp[i-1][1]+1
        dp[i][1] = dp[i-1][1] 或者 dp[i-1][0]+1
        '''
        n = len(nums)
        dp = [[0]*2 for _ in range(n)]
        dp[0][0] = 1
        dp[0][1] = 1
        for i in range(1,n):
            if nums[i]-nums[i-1] > 0:
                # 差值为正
                dp[i][0] = dp[i-1][1] + 1
            else:
                dp[i][0] = dp[i-1][0]
            if nums[i]-nums[i-1] < 0:
                dp[i][1] = dp[i-1][0] + 1
            else:
                dp[i][1] = dp[i-1][1]
        return max(dp[-1])