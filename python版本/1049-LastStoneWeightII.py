class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # @lru_cache(None)
        # def dfs(i,cur):
        #     if i == len(stones):
        #         nonlocal ans 
        #         ans = min(ans,cur)
        #     else:
        #         dfs(i+1,cur+stones[i])
        #         dfs(i+1,abs(cur-stones[i]))

        # ans = float('inf')
        # dfs(0,0)
        # return ans 
        '''
        前面这个由于数据量比较小所以可以直接使用dfs暴力求解，这个题和昨天那个非常像
        下面给出dp的思路
        '''