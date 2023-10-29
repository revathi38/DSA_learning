class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


"""
h       (none)
M -> A -> D <- A <- M      None
          s
                    f
                            curr 
                    prev
                            next

                        prev
M   ->  A   ->  D   ->  none

M   ->  A   ->  D   ->  none    
                        head                                                        
"""


def isPalindrome(head):
    # find the middle element
    slow = head
    fast = head

    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # reversing the linkedlist from middle element

    prev = None
    curr = slow

    while curr:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode

    # check head node and prev node values

    while head:
        if head.val != prev.val:
            return False
        head = head.next
        prev = prev.next

    return True


headNode = Node("M")
headNode.next = Node("M")
headNode.next.next = Node("A")
headNode.next.next.next = Node("D")
headNode.next.next.next.next = Node("A")
headNode.next.next.next.next.next = Node("M")
headNode.next.next.next.next.next.next = Node("M")
print(isPalindrome(headNode))


# TC: O(N)
# SC: O(1)
