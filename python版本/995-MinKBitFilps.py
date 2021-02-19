class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        n = len(A)
        q = collections.deque()
        ans = 0
        for i in range(n):
            if q and i >= q[0] + K:
                q.popleft()
            if len(q) % 2 == A[i]:
                if i + K > n:
                    return -1
                q.append(i)
                ans += 1
        return ans