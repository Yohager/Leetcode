n = 4
visited = [[True]*(n) for _ in range(2**n)]
#s = 'abcd'
for i in range(2**n):
    l,r = 0,n-1
    while l<r:
        while l<n and not (i & (2**l)):
            l += 1
        while r>0 and not (i & (2**r)):
            r -= 1
        if (l<r):
            visited[i] = False
            break 
        l+=1
        r-=1
print(visited)

'''
给出一个位运算枚举所有子集的模板
'''
res = []
nums = [1,2,3,4]
l = len(nums)
for i in range(1<<l):
    tmp = []
    for j in range(l):
        if ((i>>j) & 1):
            tmp.append(nums[j])
    res.append(tmp)

print(res)