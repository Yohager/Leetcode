class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s == "" or s == " ": return 0
        while s and s[-1] == ' ':
            s = s[:-1]    
        arr = list(s.split(' '))
        return len(arr[-1])
