class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_num = 0
        no_zero = []
        for i in nums:
            if i == 0:
                zero_num += 1
            else:
                no_zero.append(i)
        no_zero_num = len(nums)-zero_num
        for i in range(no_zero_num):
            nums[i] = no_zero[i]
        for j in range(no_zero_num,len(nums)):
            nums[j] = 0
        print(nums)


print(Solution.moveZeroes(Solution,[0,1,0,3,12]))
        
