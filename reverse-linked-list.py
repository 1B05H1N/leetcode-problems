class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

def a(head):
    arr = []
    while(head != None):
        arr.append(head.val) 
        head = head.next
    return arr

def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    temp = head
    print(a(head))
    print(a(reverseList(temp)))

if __name__ == "__main__":
    main()
