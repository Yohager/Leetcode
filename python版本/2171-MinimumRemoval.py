class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        n = len(beans)
        ans = float('inf')
        total = sum(beans)
        for i in range(n):
            # 左边清空，右边全部变为beans[i]的数量
            tmp = total - (n-i) * beans[i]
            ans = min(ans, tmp)
        return ans 