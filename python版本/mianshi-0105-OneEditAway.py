class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        m, n = len(first), len(second)
        if abs(m-n) > 1:
            return False 
        for i in range(min(m,n)):
            if first[i] != second[i]:
                return first[i+1:] == second[i+1:]\
                 or first[i:] == second[i+1:]\
                 or first[i+1:] == second[i:]
        return True