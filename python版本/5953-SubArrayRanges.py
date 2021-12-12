class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            minval, maxval = nums[i], nums[i]
            for j in range(i+1,n):
                # 在这个区间上的范围
                minval = min(minval, nums[j])
                maxval = max(maxval, nums[j])
                ans += maxval - minval 
        return ans 
                