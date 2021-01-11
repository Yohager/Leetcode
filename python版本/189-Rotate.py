class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k > 0:
            tmp = nums[-1]
            nums.pop(-1)
            nums.insert(0,tmp)
            k -= 1
        return nums