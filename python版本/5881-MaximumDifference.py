class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -1
        for i in range(n):
            for j in range(i+1,n):
                if nums[j] > nums[i]:
                    ans = max(ans,nums[j]-nums[i])
        return ans 