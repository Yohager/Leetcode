class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        n = len(queries)
        #做一个前缀异或
        tmp = [0,arr[0]]
        for i in range(1,len(arr)):
            x = tmp[i] ^ arr[i]
            tmp.append(x)
        
        for elem in queries:
            ans.append(tmp[elem[1]+1] ^ tmp[elem[0]])
        return ans 
