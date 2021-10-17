class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        maxval = max(arr)
        return arr.index(maxval)