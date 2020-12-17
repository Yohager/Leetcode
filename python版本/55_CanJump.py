class Solution:
    def canJump(self, nums) -> bool:
        def panduan(seq):
            if any(k > len(seq) for k in seq): return True
            else: return False
        if all([v>=1 for v in nums]): return True
        length = len(nums)
        temp = length - 2
        while (temp >= 0):
            if nums[temp] == 0:
                temp1 = temp-1
                number0 = 1
                while (temp1>=0):
                    if nums[temp1] > number0:
                        temp = temp1
                        break
                    else:
                        number0 += 1
                        temp1 -= 1
                if temp1 == -1:
                    return False
            else:
                temp -= 1
        return True



nums = [2,3,1,0,2,0,0,4]
print(Solution.canJump(Solution,nums))
