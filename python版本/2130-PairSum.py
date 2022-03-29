# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ans = 0
        arr = []
        while head:
            arr.append(head.val)
            head = head.next 
        n = len(arr)
        for i in range(n//2):
            ans = max(ans,arr[i]+arr[n-i-1])
        return ans 