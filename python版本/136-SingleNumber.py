'''
使用到的技巧
异或运算对于相同的数得到的结果是0，任何数和0做异或运算得到的结果还是他本身
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = nums[0]
        for i in range(1,len(nums)):
            temp = temp ^ nums[i]
        return temp
