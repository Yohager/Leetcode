class Solution:
    def intersection(self, nums1, nums2):
        '''
        nums1 = set(nums1)
        nums2 = set(nums2)
        m = len(nums1)
        n = len(nums2)
        if (m < n):
            result = []
            for i in nums1:
                if i  in nums2:
                    result.append(i)
        else:
            result = []
            for j in nums2:
                if j in nums1:
                    result.append(j)
        return result
        '''
        return list(set(nums1).intersection(set(nums2)))


nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(Solution.intersection(Solution,nums1,nums2))