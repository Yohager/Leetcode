class Solution:
    def firstUniqChar(self, s: str) -> int:
        chardict = {}
        for i in s:
            if i in chardict.keys():
                chardict[i] = -1
            else:
                chardict[i] = 1
        for i in range(len(s)):
            if chardict[s[i]] == 1:
                return i
        return -1