class Solution:
    def minimumMoves(self, s: str) -> int:
        n = len(s)
        top = -1
        for i in range(n):
            if s[i] == 'X':
                top = i
                break
        if top == -1:
            return 0 
        ans = 0 
        while top < n:
            if s[top] == 'X':
                ans += 1
                top += 3
            else:
                top += 1
        return ans 
                
                    