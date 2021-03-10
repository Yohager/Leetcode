class Solution:
    def calculate(self, s: str) -> int:
        ans, tmp, flag = 0,0,1
        stack = []
        for i in s:
            if i == '(':
                stack.append(ans)
                stack.append(flag)
                ans = 0
                flag = 1
            elif i.isdigit():
                tmp = 10 * tmp + int(i)
            elif i == '+' or i == '-':
                ans += flag * tmp
                tmp = 0
                flag = 1 if i == '+' else -1
            elif i == ')':
                ans += flag * tmp
                tmp = 0
                ans *= stack.pop()
                ans += stack.pop()
        ans += flag * tmp 
        return ans 