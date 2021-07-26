class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        r = len(students)
        n = len(students[0])
        res = []
        for s in students:
            tmp = []
            for m in mentors:
                cnt = 0
                for x in range(n):
                    if s[x] == m[x]:
                        cnt += 1
                tmp.append(cnt)
            res.append(tmp)
        from scipy.optimize import linear_sum_assignment
        row, col = linear_sum_assignment(res, True)
        #print(row,col)
        maxval = 0
        for i in range(len(row)):
            maxval += res[row[i]][col[i]]
        return maxval