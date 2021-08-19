class Solution:
    def checkRecord(self, s: str) -> bool:
        c = collections.Counter(s)
        if c['A'] > 2:
            return False
        n = len(s)
        for i in range(n):
            if s[i] == "L":
                if i + 2 < n and s[i+1] == "L" and s[i+2] == "L":
                    return False 
        return True 