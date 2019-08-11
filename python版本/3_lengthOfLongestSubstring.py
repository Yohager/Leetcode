#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
'''
使用暴力方法求解，遍历所有的字符子串寻找最长的不重复子串
class Solution:
    def is_unique(self,str_1):
        a = list(str_1)
        for i in a:
            if str_1.count(i) != 1:
                return False
        return True
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == None:
            return 0
        result_list = []
        for i in range(len(s)):
            for j in range(i,len(s)+1):
                #print(s[i:j])
                if self.is_unique(s[i:j]) == True:
                    result_list.append(j-i)
        if result_list == []:
            return 0
        return max(result_list)
'''
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #print('length is ',len(s))
        i = 0
        j = 0
        result = 0
        slide_window = []
        while i < len(s) and j < len(s):
            if s[j] not in slide_window:
                slide_window.append(s[j])
                j += 1
                result = max(result,len(slide_window))
            else:
                slide_window.remove(s[i])
                i += 1

        return result 
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        if s == "":
            return 0
        i = 0
        for j in range(len(s)):
            if s[j] not in s[i:j]:
                result = max(result,j-i+1)
            else:
                i += s[i:j].index(s[j]) + 1
        return result
'''
if __name__ == "__main__":
    test = Solution
    number = test.lengthOfLongestSubstring(test,"abcbda")
    print(number)
'''
