class Solution:
    @lru_cache(None)
    def countAndSay(self, n: int) -> str:
        def count(s):
            ans, cnt = [], 0
            for i,c in enumerate(s + "#"):
                if not i or s[i-1] == c:
                    cnt += 1
                if i and c != s[i-1]:
                    ans.append(str(cnt))
                    ans.append(s[i-1])
                    cnt = 1
            return "".join(ans)
        return "1" if n == 1 else count(self.countAndSay(n-1))