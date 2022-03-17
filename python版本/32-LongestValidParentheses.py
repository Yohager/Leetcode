class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        idx = 0 
        n = len(s)
        arr = [1]*n
        while idx < n:
            if not stack:
                stack.append(idx)
                idx += 1
            elif s[stack[-1]] == '(' and s[idx] == ')':
                stack.pop()
                idx += 1
            else:
                stack.append(idx)
                idx += 1
        for x in stack:
            arr[x] = 0 
        # 当前目标寻找arr数组中最长的连续的1的长度
        dp = [1 if arr[i]==1 else 0 for i in range(n)]
        for i in range(1,n):
            if arr[i] == 1:
                dp[i] = max(dp[i-1]+1,dp[i])
        return 0 if not dp else max(dp)