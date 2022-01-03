class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        arr = []
        for b in bank:
            tmp = Counter(b)
            if tmp['1'] > 0:
                arr.append(tmp['1'])
        # print(arr)
        if len(arr) == 1:
            return 0 
        else:
            ans = 0
            n = len(arr)
            for i in range(n-1):
                ans += arr[i] * arr[i+1]
            return ans 