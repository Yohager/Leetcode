class Solution:
    def searchInsert(self, nums, target) -> int:
        if (target > nums[-1]):
            return len(nums)
        start = 0
        end = len(nums) - 1
        while (start < end):
            mid = (start + end) // 2
            if (nums[mid] == target):
                return mid
            elif (nums[mid] < target):
                start = mid + 1
            else:
                end = mid
        return start

if __name__ == "__main__":
    test = Solution
    nums = [1,3,5,6]
    target = 7
    print(test.searchInsert(test,nums,target))