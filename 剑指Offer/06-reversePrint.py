# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
可以使用本科数据结构中学到的链表的就地逆置（有点忘了……）
反正这个题目是一定要遍历两边的
可以考虑用栈或者用递归，也可以就地逆置链表
'''
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        temp = head
        result = []
        while temp != None:
            result.append(temp.val)
            temp = temp.next
        return list(reversed(result))
