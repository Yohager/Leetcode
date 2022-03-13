'''
确定k的取值范围
对于数组中的任意一个元素x
如果x > i(i表示x的初始下标) 如果k要得分则范围是: i+1 <= k <= n+i-x
如果x <= i 如果k要得分则范围是: k <= i-x 或者 k >= i+1
整体来看范围是 0到i-x和i+1到n+i-x
对于每一个元素都可以计算k的范围
遍历所有元素即可知道每个轮调下标的对应的计1分的个数
分数最高的即为结果
当 i < x 时: 符合条件的是 [i+1,n+i-x]
当 i >= x时: 符合条件的是 [0,i+1], [i-x,n-1]
定义长度为n的diffs数组
diffs[k] = points[k] - points[k-1]
'''
def solution(nums):
    n = len(nums)
    diff = [0] * n
    for i, num in enumerate(nums):
        low = (i+1) % n 
        high = (n+i-num+1) % n
        diff[low] += 1
        diff[high] -= 1
        if low <= high:
            diff[0] += 1
    pt,mv,idx = 0,0,0
    for i,dif in enumerate(diff):
        pt += dif 
        if pt > mv:
            mv = pt 
            idx = i 
    return idx 

