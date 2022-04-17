class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        if len(tasks) <= 1:
            return -1 
        c = Counter(tasks)
        ans = 0
        for k in c.keys():
            v = c[k]
            if v == 1:
                return -1 
            elif v == 2 or v == 3:
                ans += 1
            else:
                # 超过3的情况
                cnt = v // 3 
                left = v % 3 
                if not left:
                    ans += cnt 
                else:
                    ans += cnt+1
        return ans 