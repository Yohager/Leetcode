#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        row_gap = numRows - 2
        a = len(s) // (numRows + row_gap)
        b = len(s) % (numRows + row_gap)
        #print(a,b)
        if 0 < b <= numRows:
            col_nums = a *(1 + row_gap) + 1
        elif b == 0:
            col_nums = a *(1 + row_gap)
        else:
            col_nums = a *(1 + row_gap) + (b - numRows)
        z_matrix = [[0 for _ in range(col_nums)] for _ in range(numRows)]
        #print(col_nums)
        #给矩阵填数据
        for i in range(col_nums):
            if i % (row_gap+1) == 0:
                z_matrix[i] = s[(row_gap+1)*i:(row_gap+1)*i+numRows]
            else:
                z_matrix[i][numRows-1-int(i%(row_gap+1))] = s[i*numRows + int(i%(row_gap+1))]
        return z_matrix




print(Solution.convert(Solution,"LEETCODEISHIRING",4))
