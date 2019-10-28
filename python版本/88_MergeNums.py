class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr_1 = 0
        ptr_2 = 0
        temp = nums1[:m]
        #print(temp)
        new_list = []
        while (ptr_1 < m  and ptr_2 < n):
            if (temp[ptr_1] < nums2[ptr_2]):
                new_list.append(temp[ptr_1])
                ptr_1 += 1
            else:
                new_list.append(nums2[ptr_2])
                ptr_2 += 1
        new_list += temp[ptr_1:]
        new_list += nums2[ptr_2:]
        #print(new_list)
        for i in range(len(new_list)):
            nums1[i] = new_list[i]


if __name__ == "__main__":
    test = Solution
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    test.merge(test,nums1,3,nums2,3)
    print(nums1)


