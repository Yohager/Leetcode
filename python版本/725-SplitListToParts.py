# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        ans = []
        arr = []
        tmp = head 
        while tmp:
            arr.append(tmp.val)
            tmp = tmp.next 
        
        n = len(arr)
        times = n // k 
        left = n % k 
        nums = [times]*k 
        for i in range(left):
            nums[i] += 1
        idx = 0
        #print(nums)
        for j in range(k):
            #print(j,idx)
            tmp = []
            if idx >= len(arr):
                ans.append(None)
                continue
            new_h = ListNode(arr[idx])
            a = new_h
            idx += 1
            steps = nums[j] - 1
            while steps > 0:
                temp = ListNode(arr[idx])
                a.next = temp 
                a = temp 
                steps -= 1
                idx += 1
            ans.append(new_h)
        return ans 