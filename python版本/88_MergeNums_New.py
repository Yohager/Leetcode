class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr1 = m - 1
        ptr2 = n - 1
        temp = m + n -1
        while (ptr1 >= 0 and ptr2 >= 0):
            if (nums1[ptr1] >= nums2[ptr2]):
                nums1[temp] = nums1[ptr1]
                ptr1 -= 1
            else:
                nums1[temp] = nums2[ptr2]
                ptr2 -= 1
            temp -= 1
        nums1[:ptr2 + 1] = nums2[:ptr2 + 1]

if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]