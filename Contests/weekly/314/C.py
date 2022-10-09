class Solution:
    def robotWithString(self, s: str) -> str:
        ans = ''
        stack = []
        cnt = Counter(s)
        rec = 97
        for x in s:
            cnt[x] -= 1
            # 找尚未入栈的最小的字母
            while rec <= 123 and cnt[chr(rec)] <= 0:
                rec += 1
            stack.append(x)
            while stack and stack[-1] <= chr(rec):
                ans += stack.pop()
        return ans 
