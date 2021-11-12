class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        import math
        tmp = int(math.sqrt(num))
        if tmp * tmp == num:
            return True
        else:
            return False