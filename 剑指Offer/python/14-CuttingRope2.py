class Solution:
    def cuttingRope(self, n: int) -> int:
        '''
        不要进行大数运算，因为会出现溢出的情况
        '''
        if n <= 3:
            return n-1
        else:
            result = 1
            while (n > 4):
                result *= 3
                result = result % (1e9+7)
                n -= 3
        return int(result * n % (1e9+7))