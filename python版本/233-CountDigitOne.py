class Solution:
    def countDigitOne(self, n: int) -> int:
        cnt = 0
        i = 1 
        while i <= n:
            tmp1 = n // i 
            tmp2 = n % i 
            cnt += (tmp1+8) // 10 * i + (tmp1 % 10 == 1) * (tmp2+1)
            i *= 10 
        return cnt 