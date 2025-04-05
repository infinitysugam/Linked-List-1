# Time Complexity = O(n)
# Space Complexity = O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        fast = head 
        slow = head 
        prev = None

        for i in range(0,n):
            fast = fast.next

        if not fast:
            return head.next
        
        while fast!=None:
            prev = slow
            slow = slow.next
            fast = fast.next
        
        #print(slow.val)
        prev.next = slow.next
        return head

    
        
        