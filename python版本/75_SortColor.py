class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        count_list = [0,0,0]
        for i in nums:
            if i == 0:
                count_list[0] += 1
            elif i == 1:
                count_list[1] += 1
            else:
                count_list[2] += 1
        for j in range(count_list[0]):
            nums[j] = 0
        for k in range(count_list[1]):
            nums[k+count_list[0]] = 1
        for m in range(count_list[2]):
            nums[m+count_list[0]+count_list[1]] = 2
