class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def findMiddleNode(self, root):
        if not root:
            return root

        slow_pointer = root.next
        fast_pointer = root.next.next

        while fast_pointer.next and fast_pointer.next.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        return slow_pointer


# Example usage
# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)


# Find the middle node
LL = LinkedList()
middle_node = LL.findMiddleNode(head)

print("Middle node:", middle_node.val)
