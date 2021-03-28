# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head 

        if head.val == head.next.val:
            tmp = head.next
            while tmp.next and head.val == tmp.next.val:
                tmp = tmp.next
            return self.deleteDuplicates(tmp)
        else:
            head.next = self.deleteDuplicates(head.next)
        return head