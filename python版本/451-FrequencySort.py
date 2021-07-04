class Solution:
    def frequencySort(self, s: str) -> str:
        c = collections.Counter(s)
        n = len(c.keys())
        ans = ''
        for x in c.most_common(n):
            ans += x[0] * x[1]
        return ans 