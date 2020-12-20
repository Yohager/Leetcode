from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s) == 0:
            return t
        s_1 = Counter(s)
        t_1 = Counter(t)
        for key in t_1.keys():
            if key not in s_1.keys():
                return key
            else:
                if t_1[key] != s_1[key]:
                    return key