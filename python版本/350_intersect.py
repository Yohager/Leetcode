class Solution:
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        result = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return result


nums1 = [1,2]
nums2 = [1,1]

print(Solution.intersect(Solution,nums1,nums2))
