class Solution:
    def search(self, nums, target) -> int:
        #采用二分查找的方法
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            #向后重复循环的情况 
            if (nums[mid] >= nums[start]) and (target > nums[mid] or target < nums[start]):
                start = mid + 1
            elif (nums[mid] < nums[start]) and (target < nums[start] and target > nums[mid]):
                start = mid + 1
            else:
                end = mid
            
        if start == end and nums[start] == target:
            return start
        else:
            return -1
    

if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    target = 4
    test = Solution
    print(test.search(test,nums,target))



