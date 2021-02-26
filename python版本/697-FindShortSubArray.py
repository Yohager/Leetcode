class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left, right = dict(), dict()
        counter = collections.Counter()
        for i, num in enumerate(nums):
            if num not in left:
                left[num] = i
            right[num] = i
            counter[num] += 1
        degree = max(counter.values())
        res = len(nums)
        for k, v in counter.items():
            if v == degree:
                res = min(res, right[k] - left[k] + 1)
        return res