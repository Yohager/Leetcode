class Solution:
    def maxSubArray(self, nums) -> int:
        '''
        暴力解法
        if len(nums) == 1:
            return nums[0]
        max_num = [-100,0,0]
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if sum(nums[i:j+1]) > max_num[0]:
                    max_num[0] = sum(nums[i:j+1])
                    max_num[1] = i
                    max_num[2] = j
        return max_num
        '''
        '''
        优化前缀和
        length = len(nums)
        max_sum = nums[0]
        min_sum = sum_num = 0
        for i in range(length):
            sum_num += nums[i]
            max_sum = max(max_sum,sum_num - min_sum)
            min_sum = min(min_sum,sum_num)
        return max_sum
        '''
        



if __name__ == "__main__":
    test = Solution()
    print(test.maxSubArray([1,2]))
            