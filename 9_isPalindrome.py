#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#
import operator
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        result = list(map(int,str(x)))
        #print(result)
        length = len(result)
        result_reverse = result[:]
        result_reverse.reverse()
        print(result)
        print(result_reverse)
        return operator.eq(result,result_reverse)

    
'''
if __name__ == "__main__":
    test = Solution
    print(test.isPalindrome(test,10))
'''
