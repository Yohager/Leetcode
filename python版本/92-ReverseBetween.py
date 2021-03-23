# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(0)
        #用于保存这个head
        dummy.next = head 
        tmp1,tmp2 = dummy,None
        for i in range(left-1):
            tmp1 = tmp1.next
        head = tmp1.next
        print(head.val)
        #head指针指向的位置是需要翻转的起始点，tmp1表示的是前驱节点
        for j in range(left,right):
            tmp2 = head.next
            head.next = tmp2.next 
            tmp2.next = tmp1.next 
            tmp1.next = tmp2
        return dummy.next 
            