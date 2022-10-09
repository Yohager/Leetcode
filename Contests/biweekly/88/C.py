class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        if n1 % 2 == 0 and n2 % 2 == 0:
            return 0
        elif n1 % 2 == 0 and n2 % 2 != 0:
            res = nums1[0]
            for i in range(1, n1):
                res ^= nums1[i]
            return res 
        elif n1 % 2 != 0 and n2 % 2 == 0:
            res = nums2[0]
            for i in range(1, n2):
                res ^= nums2[i]
            return res 
        else:
            res = nums1[0]
            for i in range(1, n1):
                res ^= nums1[i]
            for j in range(n2):
                res ^= nums2[j]
            return res 