class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def funck(i,j):
            num1 = list(map(int,list(str(i))))
            num2 = list(map(int,list(str(j))))
            return sum(num1)+sum(num2)

        if k == 0:
            return 1
        result = [[(k+1) for _ in range(n+2)] for _ in range(m+2)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                result[i][j] = funck(i-1,j-1)
        return result


m,n,k=16,8,4
Solution.movingCount(Solution,m,n,k)