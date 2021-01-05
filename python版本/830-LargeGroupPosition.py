class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        if s == '': return []
        ans = []
        n = len(s)
        i = 0
        while i < n:
            j = i + 1
            while j < n and s[j] == s[i]:
                j += 1
            if (j-1) - i >= 2:
                ans.append([i,j-1])
                i = j
            i = j
        return ans
