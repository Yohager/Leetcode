class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0 
        dp = [0] * n 
        ans = 0
        if nums[1]-nums[0] == nums[2]-nums[1]:
            dp[2] = 1
        for i in range(3,n-1):
            if nums[i]-nums[i-1] == nums[i+1]-nums[i]:
                dp[i] = dp[i-1] + 1
                tmp += 1
                ans += tmp 
            else:
                tmp = 0
        return ans