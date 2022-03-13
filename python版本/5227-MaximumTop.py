class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if k == 0:
            return nums[0]
        n = len(nums)
        if n == 1: #特判一下当n为1的情况
            return -1 if k % 2 != 0 else nums[0]
        # 考虑k > n 可以将所有的元素全部pop出
        if k == 1:
            if len(nums) == 1:
                return -1
            else:
                return nums[1]
        if k > n:
            # left = k - n # 将所有元素pop出来的剩余操作次数
            return max(nums)
        # 讨论k小于n的情况
        '''
        考虑第k个位置的元素
        '''
        if n == k:
            return max(nums[:k-1])
        else:
            v = nums[k] # pop掉k个值取栈顶元素
            arr = nums[:k-1] # 弹出前k-1个再放回最大的一个
            return max(v,max(arr))