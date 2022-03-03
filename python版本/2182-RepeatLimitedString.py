class Solution:
    def repeatLimitedString(self, s: str, r: int) -> str:
        d = OrderedDict()
        for x in sorted(list(s),reverse=True):
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1
        # print(d)
        ans = ''
        keys = list(d.keys())
        idx = 0
        while idx < len(keys):
            if d[keys[idx]] == 0:
                idx += 1
            elif d[keys[idx]] <= r:
                ans += keys[idx] * d[keys[idx]]
                d[keys[idx]] = 0
            else:
                ans += keys[idx] * r 
                d[keys[idx]] -= r 
                tmp = idx + 1 
                while tmp < len(keys):
                    if d[keys[tmp]] >= 1:
                        ans += keys[tmp]
                        d[keys[tmp]] -= 1
                        break 
                    else:
                        tmp += 1
                if tmp == len(keys):
                    break 
                
        return ans 
                
                
                
            
        