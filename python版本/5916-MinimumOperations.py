class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        MAXSIZE = 1001
        dist = [0] * MAXSIZE
        q = collections.deque()
        vis = set()
        q.append(start)
        while q:
            tmp = q.popleft()
            vis.add(tmp)
            for num in nums:
                if tmp + num >= 0 and tmp + num <= 1000:
                    if tmp + num not in vis:
                        vis.add(tmp+num)
                        q.append(tmp+num)
                        dist[tmp+num] = dist[tmp] + 1
                if tmp - num >= 0 and tmp - num <= 1000:
                    if tmp - num not in vis:
                        vis.add(tmp-num)
                        q.append(tmp-num)
                        dist[tmp-num] = dist[tmp] + 1
                if tmp ^ num >= 0 and tmp ^ num <= 1000:
                    if tmp ^ num not in vis:
                        vis.add(tmp^num)
                        q.append(tmp^num)
                        dist[tmp^num] = dist[tmp] + 1
        if goal >= 0 and goal <= 1000:
            if goal not in vis:
                return -1 
            return dist[goal]
        
        ans = -1
        for num in nums:
            cur = goal - num
            if cur >= 0 and cur <= 1000 and cur in vis:
                if ans == -1 or ans > dist[cur] + 1:
                    ans = dist[cur] + 1
            cur = goal + num
            if cur >= 0 and cur <= 1000 and cur in vis:
                if ans == -1 or ans > dist[cur] + 1:
                    ans = dist[cur] + 1
            cur = goal ^ num 
            if cur >= 0 and cur <= 1000 and cur in vis:
                if ans == -1 or ans > dist[cur] + 1:
                    ans = dist[cur] + 1
        return ans 
        


if __name__ == "__main__":
    a = [1,3]
    b = 6
    c = 4
    print(Solution.minimumOperations(Solution,a,b,c))