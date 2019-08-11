#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
class Solution:
    def twoSum(self, nums: list, target: int):
        for i in range(len(nums)):
            if (target - nums[i]) in nums and nums.index(target-nums[i]) != i:
                return [i,nums.index(target-nums[i])]
                
'''
if __name__ == "__main__":
    test = Solution
    result = test.twoSum(test,[3,2,4],6)
    print(result)
'''
