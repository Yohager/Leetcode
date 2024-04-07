class Solution:
    def finalString(self, s: str) -> str:
        ans = ""
        for x in s:
            if x == "i":
                ans = ans[ : : -1]
            else:
                ans += x
        return ans 
