class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        return min(ops, key = lambda x: x[0])[0] * min(ops, key = lambda x: x[1])[1] if ops else m * n