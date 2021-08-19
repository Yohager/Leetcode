class Solution:
    def countArrangement(self, n: int) -> int:
        '''
        先明确一下：a被b整除的意思是: a/b为整数
        nums[i] / i 为整数
        i / nums[i] 为整数
        '''
        match = [[] for _ in range(n+1)]
        visit = [False for _ in range(n+1)]
        ans = 0
        def backtrack(idx,n):
            if idx == n+1:
               nonlocal ans 
               ans += 1
               return 
            for x in match[idx]:
                if not visit[x]:
                    visit[x] = True 
                    backtrack(idx+1,n)
                    visit[x] = False 
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i % j == 0 or j % i == 0:
                    match[i].append(j)

        backtrack(1,n)
        return ans 
