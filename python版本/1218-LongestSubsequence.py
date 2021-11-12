class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        d = {}
        for x in arr:
            d[x] = d.get(x - difference, 0) + 1
        return max(d.values())