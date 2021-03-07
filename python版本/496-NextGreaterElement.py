class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        indexs = []
        ans = [-1 for _ in range(len(nums1))]
        n = len(nums2)
        for i in nums1:
            for j in range(n):
                if i == nums2[j]:
                    indexs.append(j)
        for i in range(len(nums1)):
            for k in range(indexs[i],n):
                if nums2[k] > nums1[i]:
                    ans[i] = nums2[k]
                    break
        return ans 