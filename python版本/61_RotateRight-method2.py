# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head 
        d = head 
        count = 1
        while d.next:
            d = d.next
            count += 1
        #print(count)
        k = count - k % count - 1
        #d指针已经指向了最后一个元素
        #下面考虑移动另一个指针
        #print(d.val)
        d.next = head 
        tmp1 = head
        while k > 0:
            tmp1 = tmp1.next 
            k -= 1
        ans = tmp1.next 
        tmp1.next = None
        return ans