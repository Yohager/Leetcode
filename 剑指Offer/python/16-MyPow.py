class Solution:
    def myPow(self, x: float, n: int) -> float:
        '''
        使用快速幂算法
        如果用一般的算法会超时
        将一个十进制数表示为二进制数，所有的1表示一次在ans上的累乘，而每一次移位就要在x上做自乘
        '''
        ans = 1
        if x == 0: return 0
        if n == 0: return 1
        if n < 0: 
            x,n = 1/x, -n
        while n:
            if n & 1: ans *= x
            x *= x
            n >>= 1
        return ans