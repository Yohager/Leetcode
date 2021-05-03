class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        r = int(math.sqrt(c))
        l = 0
        while l <= r:
            tmp = l*l + r*r
            if tmp > c:
                r -= 1
            elif tmp < c:
                l += 1
            else:
                return True
        return False