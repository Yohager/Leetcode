class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        def bischeck(nums,t):
            l,r = 0,len(nums)-1
            while l <= r:
                m = (l+r) // 2
                if nums[m] < t:
                    r = m - 1
                else:
                    l = m + 1
            return l
        ans1 = 0
        for i in range(n1):
            tmp1 = bischeck(nums2,nums1[i])
            if i <= tmp1 - 1:
                ans1 = max(ans1,tmp1-i-1)
        return ans1