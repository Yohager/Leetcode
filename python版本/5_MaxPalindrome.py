#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
'''
暴力求解法
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
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == "" or len(s) == 1:
            return s
        bool_matrix = [[0 for i in range(len(s))] for j in range(len(s))]
        #print(bool_matrix)
        start = 0
        max_num = 1
        for i in range(len(s)):
            bool_matrix[i][i] = 1
            if i < len(s)-1 and s[i] == s[i+1]:
                bool_matrix[i][i+1] = 1
                max_num = 2
                start = i
        #print(bool_matrix)
        for length in range(3,len(s)+1):
            for j in range(len(s) - length + 1):
                k = j + length -1
                if s[j] == s[k] and bool_matrix[j+1][k-1] == 1:
                    bool_matrix[j][k] = 1
                    start = j
                    max_num = length
        return s[start:start+max_num]

'''
if __name__ == "__main__":
    test = Solution
    print(test.longestPalindrome(test,"babad"))
'''
