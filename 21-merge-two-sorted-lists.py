class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        list1Ptr = list1
        list2Ptr = list2
        listFinal = ListNode(0)
        dummy = listFinal 
        while list1Ptr is not None and list2Ptr is not None:
            list1Value = list1Ptr.val
            list2Value = list2Ptr.val
            if list1Value < list2Value:
                dummy.next = list1Ptr
                list1Ptr = list1Ptr.next
            else:
                dummy.next = list2Ptr
                list2Ptr = list2Ptr.next
            dummy = dummy.next
        if list2Ptr is None:
            dummy.next = list1Ptr
        if list1Ptr is None:
            dummy.next = list2Ptr
        return listFinal.next
