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
        #尝试使用分治思想的方法
        length = len(nums)
        if length == 1:
            return nums[0]
        else:
            max_left = self.maxSubArray(nums[:length // 2])
            max_right = self.maxSubArray(nums[length // 2 : ])
        #下面计算中间最大子序列
        max_l = nums[length // 2 -1]
        temp = 0
        for i in range(length // 2 -1,-1,-1):
            temp += nums[i]
            max_l = max(temp,max_l)
        max_r = nums[length // 2]
        temp = 0
        for j in range(length // 2, length):
            temp += nums[j]
            max_r = max(temp,max_r)
        return max(max_left,max_right,max_l+max_r)



if __name__ == "__main__":
    test = Solution()
    print(test.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
            