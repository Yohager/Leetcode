class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        sum1 = sum(nums)
        diff = abs(sum1-goal)
        #print(diff)
        if diff == 0:
            return 0
        if diff <= limit:
            return 1
        if diff % limit == 0:
            return diff // limit 
        else:
            return diff // limit + 1