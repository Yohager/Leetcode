class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        arr = s.split(' ')
        nums =[]
        for x in arr:
            if x.isdigit():
                nums.append(int(x))
        for i in range(1,len(nums)):
            if nums[i-1] >= nums[i]:
                return False 
        return True 