class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def ntok(val):
            ans = ''
            while val:
                ans += str(val % k)
                val //= k 
            return ans 
        
        def check(s):
            l,r = 0, len(s)-1
            while l < r:
                if s[l] != s[r]:
                    return False 
                else:
                    l += 1 
                    r -= 1
            return True 
        
        idx = 1
        res = 0 
        cnt = 0 
        r = 1
        flag = True
        while cnt < n:
            if idx == 10 ** r:
                if flag:
                    flag = False 
                    idx //= 10
                else:
                    flag = True 
                    r += 1
            s = str(idx)
            if flag:
                val = s[:-1] + s[::-1]
            else:
                val = s + s[::-1]
            if check(ntok(int(val))):
                cnt += 1
                res += int(val)
            idx += 1
        return res 