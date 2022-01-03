class Solution:
    def checkString(self, s: str) -> bool:
        if 'b' not in s:
            return True
        idx = s.index('b')
        # print(idx)
        for x in s[idx+1:]:
            if x == 'a':
                return False 
        return True