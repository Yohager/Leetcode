#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if strs == []:
            return ""
        result = ""
        length_list = [len(k) for k in strs]
        length = min(length_list)
        temp = []
        for i in range(length):
            for j in range(len(strs)):
                temp.append(strs[j][i])
            if len(set(temp)) == 1:
                result += list(set(temp))[0]
                temp = []
            else:
                temp = []
                break
        return result

                
#print(Solution.longestCommonPrefix(Solution,["aca","cba"]))

        

