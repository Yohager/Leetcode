'''
quick sort
在array中选择一个pivot位置
将小于pivot的元素放在pivot的左边
将大于pivot的元素放在pivot的右边
左边与右边两个部分分别进行递归处理
'''
import random 
import time 

def QuickSort(arr):
    if len(arr) < 2:
        return arr 
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [y for y in arr[1:] if y >= pivot]
        return QuickSort(left) + [pivot] + QuickSort(right)

'''
quick sort
第二种实现方式
原地修改数组,不占用额外的空间
'''
def QuickSort2(arr,l,r):
    if l >= r:
        return 
    low, high = l,r 
    pivot = arr[low]
    while low < high:
        while (low < high and arr[high] >= pivot):
            # 从后向前扫描一次 找到第一个小于pivot的值
            high -= 1
        arr[low] = arr[high]
        while (low < high and arr[low] < pivot):
            # 从前向后扫描一次找到第一个大于pivot的值
            low += 1
        arr[high] = arr[low]
    arr[low] = pivot
    QuickSort2(arr,l,low-1)
    QuickSort2(arr,low+1,r)


if __name__ == "__main__":
    arr = [random.randint(1,1000000) for _ in range(1000000)]
    start = time.time()
    print(QuickSort(arr))
    # QuickSort2(arr,0,len(arr)-1)
    # print(arr)
    end = time.time()
    print(end-start)