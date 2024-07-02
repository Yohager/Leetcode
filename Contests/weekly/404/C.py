class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        '''
        observation 
        找出的序列一定满足 a,b,a,b,a,b,...的形式
        子序列的第一个数模k为a，第二数模k为b，第三个数一定模k也为a，以此类推
        从后向前 定义dp[a][b] 表示子序列最后两个数模k分别余a和b的最长子序列长度
        dp[a][b] = dp[b][a] + 1
        '''
        dp = [[0] * k for _ in range(k)]
        new_nums = [x % k for x in nums]
        for x in new_nums:
            for j in range(k):
                dp[x][j] = dp[j][x] + 1
        # print(dp)
        return max(map(max, dp))
