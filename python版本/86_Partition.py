# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        smallNode = ListNode(0)
        bigNode = ListNode(0)
        result = smallNode
        temp = bigNode
        while (head):
            if (head.val < x):
                smallNode.next = head
                smallNode = smallNode.next
            else:
                bigNode.next = head
                bigNode = bigNode.next
            head = head.next
        bigNode.next = None
        smallNode.next = temp.next
        return result.next



            



            