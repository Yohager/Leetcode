class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        hash1 = {}
        for i in nums:
            if i not in hash1:
                hash1[i] = 1
            else:
                return i