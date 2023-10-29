class Node:
    def __init__(self, data, next = None):
        self.val = data
        self.next = next

def detectCycle(head):
    if not head:
        return head

    slow_pointer = head
    fast_pointer = head

    while fast_pointer and fast_pointer.next and fast_pointer.next.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

        if slow_pointer == fast_pointer:
            return True

    return False


# Example usage
# Create a linked list with a cycle: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 3 (connecting back to node 3)
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = head.next.next  # Creating a cycle


# Detect cycle in the linked list
has_cycle = detectCycle(head)

if has_cycle:
    print("Cycle detected in the linked list.")
else:
    print("No cycle detected in the linked list.")