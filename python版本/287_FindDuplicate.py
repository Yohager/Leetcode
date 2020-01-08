class Solution:
    def findDuplicate(self, nums) -> int:
        '''
        算法的思想大概是使用两个指针
        '''
        i = nums[0]
        j = nums[0]
        while True:
            i = nums[i]
            j = nums[nums[j]]
            if i == j:
                break
        ptr1 = nums[0]
        ptr2 = i 
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]
        return ptr1


print(Solution.findDuplicate(Solution,[1,3,4,2,2]))