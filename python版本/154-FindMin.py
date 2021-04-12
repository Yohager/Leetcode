class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        l,r = 0,n-1
        ans = float('inf')
        while l <= r:
            m = (l+r) // 2
            if nums[l] == nums[r] and l != r:
                l += 1
                continue
            ans = min(ans,nums[m])
            if nums[m] > nums[r]:
                #左边是有序的且是单调不减的
                l = m + 1 
            else:
                r = m - 1
        return ans 