class Solution:
    def firstUniqChar(self, s: str) -> str:
        from collections import OrderedDict
        d = OrderedDict()
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for k in d:
            if d[k] == 1:
                return k
        return " "