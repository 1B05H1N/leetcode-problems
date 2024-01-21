# This code defines a method `isPalindrome` in the `Solution` class to determine
# if a singly-linked list is a palindrome (reads the same forwards and backwards).

# 1. Edge Case Check:
#    - Checks if the input `head` is `None`. Returns `False` for a non-existent list.

# 2. Finding the Middle of the Linked List:
#    - Uses two pointers, `slow` and `fast`. `slow` moves one node at a time, while
#      `fast` moves two nodes at a time.
#    - When `fast` reaches the end, `slow` will be at the middle of the list.

# 3. Reversing the Second Half of the List:
#    - Splits the list into two halves and reverses the second half in-place.
#    - Uses `prev` to track the previous node and `curr` for the current node,
#      starting from the middle. Reverses the links in the second half.

# 4. Comparing the Two Halves:
#    - After reversal, `prev` points to the head of the reversed second half,
#      and `head` to the head of the first half.
#    - Compares values of corresponding nodes in both halves.
#    - If any pair of nodes has different values, returns `False`.
#    - If all pairs match, returns `True`, indicating the list is a palindrome.

# This approach is efficient, traversing the list a maximum of two times and
# performing the reversal in-place without extra space.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
            if head is None:
                return false 

            # declare slow and fast     
            slow = head
            fast = head.next
            
            # get the middle
            while slow and fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            middle = slow
            
            # reverse 2nd half of linked-list
            prev = None
            curr = middle.next
            while curr:
                # reverse
                next = curr.next
                # curr.next will point to prev node
                curr.next = prev
                # prev will become the current node
                prev = curr
                # curr will be the next node
                curr = next
                
            # prev is second half of linked-list reversed
            # compare the first half of the lsit with the 2nd half
            while prev and head:
                # compare values of nodes 
                if head.val != prev.val:
                    return False
                head = head.next
                prev = prev.next
            return True
