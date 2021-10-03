class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        total_num = m * n 
        num = len(original)
        if num != total_num:
            return []
        ans = []
        times = 0
        for i in range(0,num,n):
            ans.append(original[i:i+n])
        return ans 