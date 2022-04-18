class Solution:
    def minimumSum(self, num: int) -> int:
        nums = list(map(int,str(num)))
        # print(nums)
        tmp1,tmp2 = '',''
        nums.sort()
        # print(nums)
        n = len(nums)
        for i in range(n):
            if i % 2 == 0:
                tmp1 += str(nums[i])
            else:
                tmp2 += str(nums[i])
        return int(tmp1) + int(tmp2)