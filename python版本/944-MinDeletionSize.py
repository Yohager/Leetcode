class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        matrix = []
        for s in strs:
            cur = [ord(e) for e in s]
            matrix.append(cur)
        
        ans = 0
        n = len(strs[0])
        for j in range(n):
            tmp = [x[j] for x in matrix]
            if tmp != sorted(tmp):
                ans += 1
        return ans 