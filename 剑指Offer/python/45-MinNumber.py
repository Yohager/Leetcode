class Solution:
    def minNumber(self, nums: List[int]) -> str:
        return "".join(sorted([str(i) for i in nums], key=cmp_to_key(lambda a,b:1 if a+b > b+a else -1)))