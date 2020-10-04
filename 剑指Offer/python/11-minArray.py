class Solution:
    def minArray(self, numbers: List[int]) -> int:
        #基本思路是折半查找
        low = 0
        high = len(numbers)-1
        while low < high:
            mid = (low + high) // 2
            #如果最右边的数大于中间的数一定说明右半边一定是有序数组
            if (numbers[high] > numbers[mid]):
                high = mid
            elif (numbers[high] < numbers[mid]):
                low = mid + 1
            else:
                high -= 1
        return numbers[low]