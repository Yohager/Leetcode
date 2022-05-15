class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = list(str(num))
        n = len(s)
        ans = 0
        for i in range(0,n-k+1):
            cur = int(''.join(s[i:i+k]))
            # print(cur)
            if cur == 0:
                continue 
            else:
                if num % cur == 0:
                    ans += 1
        return ans 