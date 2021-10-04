class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total = mean * (m+n)
        s1 = sum(rolls)
        diff = total - s1
        if diff < n or diff > 6*n:
            return []
        times = diff // n 
        left = diff % n 
        res = [times]*n
        for i in range(left):
            res[i] += 1
        return res 
        