class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            tmp = list(str(x))
            tmp.reverse()
            ans = int(''.join(tmp))
        else:
            tmp = list(str(abs(x)))
            tmp.reverse()
            ans = (-1) * int(''.join(tmp))
        
        if ans > 2**31 - 1 or ans < -2**31:
            return 0
        else:
            return ans