class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        arr = list(s)
        cnt = 0
        n = len(arr)
        idx = 0
        while idx < n//2:
            l = idx
            r = n - l - 1
            while arr[l] != arr[r]:
                r -= 1
                # 这里表示出现了单独的一个字符
            if l == r:
                # 表示是一个单独的字符，应该放在中间
                arr[l],arr[l+1] = arr[l+1],arr[l]
                cnt += 1
                idx -= 1
            else:
                for j in range(r,n-l-1):
                    arr[j],arr[j+1] = arr[j+1], arr[j]
                    cnt += 1
            idx += 1
        return cnt