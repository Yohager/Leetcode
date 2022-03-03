class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        '''
        下标映射
        2013  0123 
        '''
        d = {}
        for i,x in enumerate(nums1):
            d[x] = i 
        arr = []
        for n in nums2:
            arr.append(d[n])
        # print(arr)
        # 遍历nums2 左边小于nums2[i]的值，右边大于nums2[i]的值
        ans = 0
        from sortedcontainers import SortedList 
        l = SortedList()
        n = len(nums2)
        for i in range(1,n-1):
            l.add(arr[i-1])
            tmp = arr[i]
            smaller = bisect.bisect_left(l,tmp)
            # print(smaller)
            # 在index为i的位置上，左边共有i+1个数，小于的有smaller个，大于的则有i+1-smaller 整个数组中大于arr[i]的数有n-arr[i]
            # 则在右边大于arr[i]的数共有：n-arr[i] - (i+1-smaller) = n-arr[i]-i-1+smaller
            ans += smaller * (n-tmp-i+smaller-1)
        return ans