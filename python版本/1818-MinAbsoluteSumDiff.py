class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        v = list(map(lambda x: abs(x[0]-x[1]), zip(nums1, nums2)))
        sum1 = sum(v)
        if sum1 == 0:
            return 0
        #先计算出当前的总差值
        #下面的思路是一个一个比较能够替换的最接近的值，使用二分查找的方式
        print(sum1)
        ans = sum1
        nums1_sort = copy.deepcopy(nums1)
        nums1_sort.sort()
        for i, num in enumerate(nums2):
            j = bisect.bisect(nums1_sort,num)
            if j < len(nums2):
                ans = min(ans,sum1-abs(nums1[i]-nums2[i])+abs(nums1_sort[j]-nums2[i]))
            if j > 0:
                ans = min(ans,sum1-abs(nums1[i]-nums2[i])+abs(nums1_sort[j-1]-nums2[i]))                
        return ans % (10**9+7)