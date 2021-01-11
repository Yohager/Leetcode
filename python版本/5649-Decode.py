class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [first]+encoded
        n = len(ans)
        for i in range(1,n):
            ans[i] = ans[i-1]^ans[i]
        return ans