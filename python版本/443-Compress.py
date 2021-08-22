class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        i = 0 
        ans = []
        while i < n:
            cur = i
            cnt = 0
            while cur < n and chars[cur] == chars[i]:
                cnt += 1
                cur += 1
            if cnt == 1:
                ans.append(chars[i])
            else:
                ans.append(chars[i])
                for x in list(str(cnt)):
                    ans.append(x)
            i = cur 
        l = len(ans)
        for i in range(l):
            chars[i] = ans[i]
        return l