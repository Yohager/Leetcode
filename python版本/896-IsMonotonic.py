class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        return True if sorted(A) == A or sorted(A,reverse=True) == A else False