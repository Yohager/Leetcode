class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        arr1 = []
        arr2 = []
        n = len(nums)
        for i in range(n):
            if i % 2 == 1:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        d1,d2 = Counter(arr1), Counter(arr2)
        c1 = d1.most_common(2)
        c2 = d2.most_common(2)
        #print(c1,c2)
        if len(c1) == 1:
            c1.append((100001,0))
        if len(c2) == 1:
            c2.append((100001,0))
        l,r = 0,0
        if c1[0][0] == c2[0][0]:
            if c1[0][1] + c2[1][1] > c1[1][1] + c2[0][1]:
                l,r = c1[0][0],c2[1][0]
            else:
                l,r = c1[1][0],c2[0][0]
        else:
            l,r = c1[0][0],c2[0][0]

        return n - d1[l] - d2[r]