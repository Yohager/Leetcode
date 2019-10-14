#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        if set(nums) == {0}:
            return [[0,0,0]]
        result = []
        nums.sort()
        for k in range(len(nums)):
            #print(k)
            i = k + 1
            j = len(nums)-1
            while i < j:
                #print(i,j,k)
                if nums[k] + nums[i] + nums[j] == 0:
                    result.append([nums[k],nums[i],nums[j]])
                    i += 1
                elif nums[k] + nums[i] + nums[j] < 0:
                    i += 1
                elif nums[k] + nums[i] + nums[j] > 0:
                    j -= 1
        result_set = list(set([tuple(t) for t in result]))
        result_set = [list(v) for v in result_set]
        return result_set
                
#print(Solution.threeSum(Solution,[-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))        

