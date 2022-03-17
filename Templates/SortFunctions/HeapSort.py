'''
heap sort 
1. 构建一个无序堆
2. heapify使得每一个最小的堆都满足堆顶元素大于/小于children元素
'''
'''
堆排序可以直接使用heapq模块中的heapify函数
heapq.heapify(list)
维护一个最小堆
'''
import heapq 
def HeapSort(arr):
    n = len(arr)
    # build the heap 
    for i in range(n // 2,-1,-1):
        heapify(arr,n,i)
    
    # exchange top and last element 
    for i in range(n-1,0,-1):
        arr[i],arr[0] = arr[0], arr[i]
        heapify(arr,i,0)
    

def heapify(arr,n,i):
    # find the largest element among root and children 
    largest = i 
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[largest] < arr[l]:
        # 如果堆顶小于左边元素 记录最大元素在左
        largest = l 
    if r < n and arr[largest] < arr[r]:
        largest = r 
    
    if largest != i:
        # heap needs to be adjusted 
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr,n,largest) # 递归调整堆

if __name__ == "__main__":
    arr = [1,4,5,7,2,9,6]
    #HeapSort(arr)
    #heapq.heapify(arr)
    nums = []
    heapq.heapify(nums)
    for a in arr:
        heapq.heappush(nums,a)
    print([heapq.heappop(nums) for _ in range(len(arr))])