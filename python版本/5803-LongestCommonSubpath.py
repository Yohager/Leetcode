from functools import lru_cache 
import sys 
sys.setrecursionlimit(999999) #限制递归的深度
class StringHash:
    def __init__(self, s, P = 1e9+7):
        self._P = P 
        self.S_hash = [0] * len(s)
        self.pow_arr = [0] * len(s)

        self.pow_arr[0] = 1
        for i in range(1,len(s)):
            self.pow_arr[i] = (self.pow_arr[i-1] * self._P) % (1 << 64)
        
        self.S_hash[0] = s[0]
        for i in range(1,len(s)):
            self.S_hash[i] = (self.S_hash[i-1] * self._P + s[i]) % (1 << 64)
    
    def get_hash(self,l,r):
        if l == 0:
            return self.S_hash[r]
        else:
            return (self.S_hash[r] - self.S_hash[l-1] * self.pow_arr[r-l+1]) % (1 << 64)

class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        min_len = 0x7fffffff
        if len(paths) <= 1:
            return 0
        
        for path in paths:
            min_len = min(min_len,len(path))
        #对于每一个path都构建一个字符串hash表
        maps = [StringHash(path) for path in paths]
        def get_hash_set(sub_len,path_idx):
            n = len(paths[path_idx])
            res = set() 
            tmp = maps[path_idx]
            for i in range(n):
                if i + sub_len <= n:
                    res.add(tmp.get_hash(i,i+sub_len-1))
                else:
                    break 
            return res
        
        def check(sub_len):
            n = len(paths)
            c = collections.Counter()
            flag = False
            for i in range(n):
                s = get_hash_set(sub_len,i)
                for val in s:
                    c[val] += 1
                    if c[val] == len(paths):
                        flag = True 
                        break 
            return flag
        
        l,r = 1, min_len
        ans = 0
        while l <= r:
            mid = (l + r) // 2 
            if check(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans 