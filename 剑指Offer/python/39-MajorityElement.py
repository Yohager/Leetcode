class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counters = collections.Counter(nums)
        return max(counters.keys(),key=lambda x:counters[x])
