class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse = True)
        s.sort(reverse = True)
        ans = 0
        index = 0
        for i in range(len(s)):
            for j in range(index,len(g)):
                if s[i] >= g[j]:
                    ans += 1
                    index = j + 1
                    break
        return ans
