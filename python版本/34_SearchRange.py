class Solution:
    def searchRange(self, nums, target):
        start = -1
        end = -1
        #考虑一些特殊情况
        if (len(nums) == 1):
            if (nums[0] == target):
                return [0,0]
            else:
                return [-1,-1]
        #使用左右指针方法进行二分查找
        p = 0
        q = len(nums) - 1
        while p <= q:
            if (p == q and nums[p] != target):
                return [-1,-1]
            mid = (p+q) // 2
            if (nums[mid] == target):
                #print("this is the mid:",mid)
                while mid > 0 and (nums[mid-1] == nums[mid]):
                    mid -= 1
                start = mid
                temp = mid
                while temp < len(nums)-1 and (nums[temp+1] == nums[temp]):
                    temp += 1
                end = temp
                return [start,end]
            elif (nums[mid] < target):
                p = mid + 1
            else:
                q = mid
        return [start,end]

if __name__ == "__main__":
    test = Solution
    nums = [5,7,7,8,8,10]
    target = 6
    print(test.searchRange(test,nums,target))