'''
使用方式是位运算中的与运算，使用与运算反复消除0.
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += 1
            n = (n-1)&n
            #print(n)
        return count