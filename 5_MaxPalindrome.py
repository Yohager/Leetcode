#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
'''
暴力求解法
'''
import operator
class Solution:
    def is_Palindrome(self,s):
        list_s = list(map(str,s))
        list_temp = list_s[:]
        list_temp.reverse()
        return operator.eq(list_s,list_temp)

    def longestPalindrome(self, s: str) -> str:
        if s == "":
            return ""
        if len(s) == 1:
            return s
        result = []
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if self.is_Palindrome(s[i:j]) == True:
                    result.append(s[i:j])
        #print(result)
        temp = None
        for k in range(len(result)):
            if temp == None:
                temp = result[k]
            if len(result[k]) >= len(temp):
                temp = result[k]
        return temp 
'''       
if __name__ == "__main__":
    test = Solution
    print(test.longestPalindrome(test,'bb'))
'''
