class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        q = deque()
        ans = 0
        n = len(fruits)
        key_idx = -1
        for idx,f in enumerate(fruits):
            if f[0] <= startPos:
                if abs(f[0]-startPos) <= k:
                    ans += f[1]
                    q.append(f)
                    key_idx = idx 
        # print(q)
        # q为空表示当前左边找不到节点
        # if not q:
        #     key_idx = -1
        tmp = ans 
        for f in fruits[key_idx+1:]:
            if startPos <= f[0] <= startPos + k:
                while q and q[0][0] < startPos and (f[0]-q[0][0] + min(startPos-q[0][0],f[0]-startPos) > k):
                   tmp -= q[0][1]
                   q.popleft()
                tmp += f[1]
                ans = max(ans, tmp)
        return ans