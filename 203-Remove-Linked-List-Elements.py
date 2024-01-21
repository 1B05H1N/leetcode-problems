# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # initialize a dummy.head
        # include head node to make things easier on us
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        curr = head
        
        # while loop through list using curr
        while curr:
            # check if curr equals our value
            if curr.val == val:
                # if it matches, remove curr by linking it to prev
                prev.next = curr.next
            else:
                # if not a match, move prev to curr 
                prev = curr
            curr = curr.next
            
        # return the head, which is dummy.next
        # this catches the use-case if our val is the first in the linked-list
        # it has to be our dummy value, otherwise it will point to Null 
        return dummy.next
