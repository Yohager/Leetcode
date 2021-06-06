class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        ans = 0
        while z:
            ans += z & 1
            z = z >> 1
        return ans 