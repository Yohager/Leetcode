class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        ans = 0
        for x in patterns:
            if x in word:
                ans += 1
        return ans