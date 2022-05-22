class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        c = Counter(s)
        cnt = c[letter]
        n = len(s)
        return (100 * cnt) // n 