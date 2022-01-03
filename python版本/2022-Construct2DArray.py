class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ans = []
        l = len(original)
        if m * n != l:
            return ans 
        for i in range(m):
            ans.append(original[i*n:(i+1)*n])
        return ans