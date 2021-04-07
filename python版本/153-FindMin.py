class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = float('inf')
        n = len(nums)
        l,r = 0,n-1
        while l <= r:
            m = (l + r) // 2
            ans = min(ans,nums[m])
            if nums[m] < nums[r]:
                r = m - 1
            else:
                l = m + 1
        return ans 