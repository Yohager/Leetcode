class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        half = len(nums)/2
        from collections import Counter
        result = Counter(nums)
        for i in result.keys():
            if result[i] > half:
                return i
        return -1