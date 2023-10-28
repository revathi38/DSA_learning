class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def splitLL(head):
    if not head or not head.next:
        return head

    mid = middleElement(head)

    next_part = mid.next

    mid.next = None

    left = splitLL(head)

    right = splitLL(next_part)

    sorted_list = merge(left, right)
    return sorted_list


def middleElement(head):
    slow = head
    fast = head

    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def merge(head1, head2):
    if not head1 and not head2:
        return None

    dummyNode = Node(0)
    curr = dummyNode

    while head1 and head2:
        if head1.val <= head2.val:
            curr.next = head1
            head1 = head1.next
        else:
            curr.next = head2
            head2 = head2.next

        curr = curr.next

    if head1:
        curr.next = head1

    if head2:
        curr.next = head2

    return dummyNode.next


def print_list(head_node):
    if not head_node:
        return None

    curr = head_node

    while curr:
        print(curr.val, end=" --> ")
        curr = curr.next
    print()


# Example usage
# Create an unsorted linked list: 4 -> 2 -> 1 -> 3 -> 5 -> None
head = Node(4)
head.next = Node(2)
head.next.next = Node(1)
head.next.next.next = Node(3)
head.next.next.next.next = Node(5)

print("Original linked list:")
print_list(head)

# Sort the linked list
sorted_head = splitLL(head)

print("Sorted linked list:")
print_list(sorted_head)

"""


1->2 -> 3 -> 4 --> none
"""
