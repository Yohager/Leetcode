class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            # print(w,str(reversed(w)))
            if w == w[::-1]:
                return w 
        return ""