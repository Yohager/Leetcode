# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        #经典快慢指针问题
        low, fast = head, head
        for i in range(k):
            fast = fast.next
        
        while fast != None:
            low = low.next
            fast = fast.next
        return low