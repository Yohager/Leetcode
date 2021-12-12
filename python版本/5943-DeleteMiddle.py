# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        tmp = head
        arr = []
        while tmp:
            arr.append(tmp.val)
            tmp = tmp.next 
        half = len(arr) // 2 
        arr.pop(half)
        # print(arr)
        new_node = ListNode(arr[0])
        ans = new_node
        idx = 1
        while idx < len(arr):
            tmp_node = ListNode(arr[idx])
            new_node.next = tmp_node
            new_node = new_node.next 
            idx += 1
        return ans 