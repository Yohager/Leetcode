class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        a = list(s.split())
        return ' '.join(a[:k])