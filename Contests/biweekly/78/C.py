class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], c: int) -> int:
        tiles.sort()
        n = len(tiles)
        ans = 0
        s = [x[0] for x in tiles]
        e = [x[1] for x in tiles]
        w = [x[1] - x[0] + 1 for x in tiles]
        f = [0] * (n+1)
        f[1] = w[0]
        for i in range(2,n+1):
            f[i] = f[i-1] + w[i-1]
        for i,x in enumerate(s):
            # 枚举起点 二分找第二个区间
            v = x + c
            idx = bisect.bisect_right(e,v-1)
            # 从i到idx位置的所有的区间长度累加
            if idx == n:
                ans = max(ans,f[-1]-f[i])
                # print(i,idx,v,f[-1]-f[i])
            else:
                # 需要额外考虑当前的这个位置有没有多出来的值
                t = f[idx] - f[i]
                if v > s[idx]:
                    t += v - s[idx]
                ans = max(ans, t)
                # print(i,idx,v,f[idx]-f[i],t)
        return ans 
