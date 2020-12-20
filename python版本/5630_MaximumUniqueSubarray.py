class Solution:
    def maximumUniqueSubarray(self, nums) -> int:
        '''
        需要总结这类题型：双指针，左端用于遍历，右端用于维护能够到达的最远的位置
        '''
        #一个用于看是否有重复数字的dict
        record_dict = {}
        for i in nums:
            record_dict[i] = 0
        total = 0
        ans = 0
        right = 0
        for left in range(len(nums)):
            if left > 0:
                record_dict[nums[left-1]] -= 1
                total -= nums[left-1]
            
            while right < len(nums) and record_dict[nums[right]] == 0:
                record_dict[nums[right]] += 1
                total += nums[right]
                right += 1
            ans = max(ans, total)
        return ans


nums = [4,2,4,5,6]

print(Solution.maximumUniqueSubarray(Solution,nums))