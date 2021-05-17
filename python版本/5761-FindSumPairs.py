class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums2 = nums2
        self.h1 = collections.Counter(nums1)
        self.h2 = collections.Counter(self.nums2)

    def add(self, index: int, val: int) -> None:
        self.h2[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.h2[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        #print(self.h2)
        cnt = 0
        for i in self.h1:
            if tot - i in self.h2:
                cnt += self.h1[i] * self.h2[tot-i]
        return cnt
        



# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)