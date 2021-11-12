# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        n = len(arr)
        temp = []
        minval = float('inf')
        for i in range(1,n-1):
            if (arr[i] > arr[i-1] and arr[i] > arr[i+1]) or (arr[i] < arr[i-1] and arr[i] < arr[i+1]):
                temp.append(i)
        if len(temp) < 2:
            return [-1,-1]
        else:
            maxval = max(temp) - min(temp)
            minval = float('inf')
            l = len(temp)
            for x in range(1,l):
                minval = min(minval,temp[x]-temp[x-1])
            return [minval,maxval]