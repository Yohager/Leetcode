class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #先对区间进行排序，保证区间左侧按照升序
        if (len(intervals) >= 2):
            intervals.sort()
        result = []
        i = 0
        j = len(intervals) - 1
        while (i <= len(intervals) - 1):
            while (i <= j):
                if (intervals[i][1] >= intervals[j][0]) and (intervals[i][0] <= intervals[j][1]):
                    result.append([intervals[i][0],intervals[j][1]])
                    break
                elif (intervals[i][1] <= intervals[j][0]) and (intervals[i][0] > intervals[j][1]):
                    result.append([intervals[j][0],intervals[j][1]])
                    break
                else:
                    j -= 1
            i = j + 1
            j = len(intervals) - 1
        return result




