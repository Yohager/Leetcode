# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None: return head
        tail = None
        while head and head.next != None:
            temp = head.next
            head.next = tail
            tail = head
            head = temp
            temp = temp.next
        head.next = tail
        return head