class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        #二维前缀异或和
        m = len(matrix)
        n = len(matrix[0])
        val = 0
        for i in range(m):
            val ^= matrix[i][0]
            matrix[i][0] = val 
        
        val = 0
        for j in range(n):
            val ^= matrix[0][j]
            matrix[0][j] = val 
        
        for i in range(1,m):
            for j in range(1,n):
                matrix[i][j] = matrix[i-1][j-1] ^ matrix[i-1][j] ^ matrix[i][j-1] ^ matrix[i][j]
        return sorted(reduce(lambda a,b :a+b, matrix),reverse=True)[k-1] 

