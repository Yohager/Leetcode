class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        idx = n-1
        while idx > 0:
            if nums[idx] > nums[idx-1]:
                # 找到第一个元素比前一个元素要大的位置
                break 
            idx -= 1
        # print(idx)
        if idx == 0:
            nums[:] = nums[::-1]
        elif idx == n-1:
            nums[idx],nums[idx-1] = nums[idx-1], nums[idx]
        else:
            minidx = idx-1
            minv = float('inf')
            for i in range(n-1,idx-1,-1):
                if nums[i] > nums[idx-1]:
                    if nums[i] < minv:
                        minv = nums[i]
                        minidx = i 
            # 将idx-1位置的元素和minidx位置的元素进行调换
            # print(minidx)
            nums[idx-1],nums[minidx] = nums[minidx], nums[idx-1]
            nums[idx:] = nums[idx:][::-1]
        
