# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            return head.next
        temp = head
        while (temp):
            if temp.next.val == val:
                temp.next = temp.next.next
                return head
            temp = temp.next
        return head

