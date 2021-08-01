class Solution:
    def search(self, nums: List[int], target: int) -> int:
        c = collections.Counter(nums)
        return c[target]