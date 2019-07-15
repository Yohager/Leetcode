#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
#
class Solution:
    def findMedianSortedArrays(self,nums1,nums2):
        length_1 = len(nums1)
        length_2 = len(nums2)
        new_list = []
        i = 0
        j = 0
        while i < length_1 and j < length_2:
            if nums1[i] <= nums2[j]:
                new_list.append(nums1[i])
                i += 1
            else:
                new_list.append(nums2[j])
                j += 1
        new_list += nums1[i:]
        new_list += nums2[j:]
        if (length_1 + length_2) % 2 == 1:
            return float(new_list[(length_1+length_2)//2])
        else:
            return float((new_list[(length_1+length_2)//2 -1] + new_list[(length_1+length_2)//2]) / 2)


'''
if __name__ == "__main__":
    nums1 = [1,2]
    nums2 = [3,4]
    test = Solution
    result = test.findMedianSortedArrays(test,nums1,nums2)
    print(result)
'''
