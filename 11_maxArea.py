#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#
'''
class Solution:
    def maxArea(self, height) -> int:
        result = []
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                result.append(min(height[i],height[j]) * (j-i))
        return max(result)
'''
class Solution:
    def maxArea(self, height) -> int:
        i = 0
        j = len(height) - 1
        result = 0
        #双指针法
        while i <= j:
            max_container = min(height[i],height[j]) * (j-i)
            if max_container >= result:
                result = max_container
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return result





#print(Solution.maxArea(Solution,[1,8,6,2,5,4,8,3,7]))
