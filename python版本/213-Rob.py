class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0],nums[1])
        dp1 = [0] * n
        dp2 = [0] * n
        dp1[1] = nums[1]
        for i in range(2,n):
            dp1[i] = max(dp1[i-1],nums[i]+dp1[i-2])

        dp2[1] = nums[0]
        for j in range(2,n):
            dp2[j] = max(dp2[j-1],nums[j-1]+dp2[j-2])
        
        return max(dp1[n-1],dp2[n-1])
        