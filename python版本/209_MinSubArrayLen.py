class Solution:
    def minSubArrayLen(self, s, nums) -> int:
        if sum(nums) < s:
            return 0
        #min_len = len(nums)
        start = 0
        result = len(nums)
        sum_nums = 0
        for i in range(len(nums)):
            sum_nums += nums[i]
            while (sum_nums >= s):
                result = min(result,i-start+1)
                sum_nums -= nums[start]
                start += 1
        return result




if __name__ == "__main__":
    nums = [1,4,4]
    s = 4
    test = Solution()
    print(test.minSubArrayLen(s,nums))


 