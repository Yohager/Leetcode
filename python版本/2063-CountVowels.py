class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        ans = 0
        for i in range(n):
            cur = 1
            if word[i] in ['a','e','i','o','u']:
                ans += (i+1) * (n-i)
        return ans 
        