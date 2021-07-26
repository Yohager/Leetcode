class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        d = {}
        for i,j in enumerate(change):
            d[str(i)] = j
        i = 0
        n = len(num)
        ans = ''
        flag = 0
        while i < n:
            if flag == 1 and d[num[i]] < int(num[i]):
                break
            elif flag == 1 and d[num[i]] >= int(num[i]):
                #当前可以进行替换了
                ans += str(d[num[i]])
            elif flag == 0 and d[num[i]] <= int(num[i]):
                ans += str(num[i])
            elif flag == 0 and d[num[i]] > int(num[i]):
                ans += str(d[num[i]])
                flag = 1
            i += 1
        ans += num[i:]
        return ans
        