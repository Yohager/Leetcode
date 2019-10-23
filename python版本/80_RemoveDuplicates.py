class Solution:
    def removeDuplicates(self, nums) -> int:
        if (len(nums) <= 2):
            return len(nums)
        max_num = nums[-1]
        start = 0
        end = 1
        count = 0
        while (end < len(nums)):
            if (nums[start] == nums[end] and count == 0):
                end += 1
                count += 1
            elif (nums[start] == nums[end] and count == 1):
                del nums[end]
            elif (nums[start] != nums[end]):
                start = end 
                end  = start + 1
                count = 0
        print(nums)
        return len(nums)

if __name__ == "__main__":
    test = Solution
    print(test.removeDuplicates(test,[1,1,1,2,2,3]))
                

