class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a = m + n -1
        l,r = m-1,n-1
        while l >= 0 and r >= 0:
            if nums1[l] > nums2[r]:
                nums1[a] = nums1[l]
                l -= 1
            else:
                nums1[a] = nums2[r]
                r -= 1
            a -= 1
        nums1[:r+1] = nums2[:r+1]
        
