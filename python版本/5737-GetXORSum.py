class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        r1,r2 = 0,0
        for i in arr1:
            r1 ^= i 
        for j in arr2:
            r2 ^= j 
        return r1 & r2
