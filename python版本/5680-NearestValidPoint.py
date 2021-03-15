class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        arr = [10000 for _ in range(len(points))]
        n = len(points)
        for i in range(n):
            if points[i][0] == x or points[i][1] == y:
                arr[i] = abs(points[i][0]-x) + abs(points[i][1]-y)
        #print(arr)
        if not arr: return -1
        tmp = min(arr)
        if tmp == 10000:
            return -1
        for i in range(n):
            if arr[i] == tmp:
                return i
        return -1