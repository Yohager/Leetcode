class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i,len(matrix[0])):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        for i in matrix:
            i.reverse()
        
        

if __name__ == "__main__":
    matrix_1 = [[1,2,3],
                [4,5,6],
                [7,8,9]]
    test = Solution
    test.rotate(test,matrix_1)
    print(matrix_1)
