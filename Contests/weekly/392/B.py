class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        n = len(s)
        # greedy from the first position 
        ans = list(s)
        idx = 0
        def calc_dist(x, y):
            return min(abs(ord(x) - ord(y)), 26 - abs(ord(x) - ord(y)))
        while idx < n and k >= 0:
            # print("check k", k)
            if k < calc_dist(ans[idx], 'a'):
                # 无法变为a了此时只能修改到这一位
                ans[idx] = chr(ord(ans[idx]) - k)
                k = -1
                break 
            else:
                k = k - calc_dist(ans[idx], 'a')
                ans[idx] = 'a'
            idx += 1
        return ''.join(ans)
            
            
