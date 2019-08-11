#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
class Solution:
    def reverse(self, x: int) -> int:
        tag = 0
        if x < 0:
            tag = 1
        x = abs(x)
        result = list(map(int,str(x)))
        #result.reverse()
        ans = 0
        for i in range(len(result)-1,-1,-1):
            #print(i)
            ans += result[i] * 10**(i)
        if tag == 1:
            ans = -ans
        if ans > 2**31 - 1 or ans < -2**31:
            return 0
        else:
            return ans

        
'''
if __name__ == "__main__":
    test = Solution
    print(test.reverse(test,123))
'''
