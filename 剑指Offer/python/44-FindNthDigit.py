class Solution:
    def findNthDigit(self, n: int) -> int:
        ans = 0
        #设置记录位次
        i = 1
        tmp = 9
        while n > tmp:
            n -= tmp
            i += 1
            tmp = 9 * i * (10 ** (i-1))
        
        #已经得到了这个n是一个几位数
        #i表示的就是几位数
        num = 10**(i-1) + (n - 1) // i 
        pos = (n - 1) % i
        return int(list(str(num))[pos])