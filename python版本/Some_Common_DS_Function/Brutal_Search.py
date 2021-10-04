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