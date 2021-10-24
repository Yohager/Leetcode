class Solution:
    def countHighestScoreNodes(self, p: List[int]) -> int:
        n = len(p)
        c = collections.defaultdict(list)
        for i,j in enumerate(p[1:],start=1):
            c[j].append(i)
        # def dfs(target):
        #     tmp = 1
        #     if target not in c:
        #         return tmp
        #     for x in c[target]:
        #         tmp += dfs(x)
        #     return tmp               
        # #cnt保存了子树的节点个数
        # maxval = n - 1
        # leafcnt = n - len(set(p)) + 1
        # ans = leafcnt
        # for node in c:
        #     val = 1 
        #     tmp = 0
        #     for child in c[node]:
        #         cnt = dfs(child)
        #         val *= cnt
        #         tmp += cnt
        #     if node != 0:
        #         val *= (n-tmp-1)
        #     if val > maxval:
        #         ans = 0
        #         maxval = val
        #     if val == maxval:
        #         ans += 1
        # return ans
        cnt = [1] * n
        def dfs(i):
            if i not in c:
                return 
            l = len(c[i])
            for j in range(l):
                dfs(c[i][j])
                cnt[i] += cnt[c[i][j]]
        dfs(0)
        #cnt存储了每一个子树的节点个数
        maxval = n - 1
        leafcnt = n - len(set(p)) + 1
        ans = leafcnt
        for x in c:
            val = 1
            tmp = 0
            for y in c[x]:
                val *= cnt[y]
                tmp += cnt[y]
            if x != 0:
                val *= (n-tmp-1)
            if val > maxval:
                ans = 0
                maxval = val
            if val == maxval:
                ans += 1
        return ans 
            
            