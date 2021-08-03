class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0
        # n = len(nums)
        # dp = [1] * n
        # '''
        # dp[i]表示到i位置的最长的严格递增子序列的长度
        # 我们此时还需要维护一个当前的最大的值
        # 如果当前新加进来的值大于前一段的最大值，那么我们就在基础上+1否则跳过
        # '''
        # ans = 1
        # for i in range(1,n):
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             dp[i] = max(1+dp[j],dp[i])
        #     ans = max(ans,dp[i])
        # return ans 
        s = []
        for x in nums:
            if not s or x > s[-1]:
                s.append(x)
            import bisect 
            idx = bisect.bisect_left(s,x)
            s[idx] = x 
        return len(s)
            



