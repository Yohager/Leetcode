class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        #return list(str(int(str(A))+K))
        tmp = ''.join(list(map(str,A)))
        return list(str(int(tmp)+K))
