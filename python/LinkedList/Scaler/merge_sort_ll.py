class Node:
    def __init__(self, data, next=None):
        self.val = data
        self.next = next


def mergeSort(h1, h2):
    if not h1 and not h2:
        return None

    dummyNode = Node(0)
    curr = dummyNode

    while h1 and h2:
        if h1.val <= h2.val:
            curr.next = h1
            h1 = h1.next
        else:
            curr.next = h2
            h2 = h2.next
        curr = curr.next

    if h1:
        curr.next = h1

    if h2:
        curr.next = h2

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
# Create the first sorted linked list: 1 -> 3 -> 5 -> 7 -> None
head1 = Node(1)
head1.next = Node(3)
head1.next.next = Node(5)
head1.next.next.next = Node(7)

# Create the second sorted linked list: 2 -> 4 -> 6 -> None
head2 = Node(2)
head2.next = Node(4)
head2.next.next = Node(6)

print("First sorted linked list:")
print_list(head1)

print("Second sorted linked list:")
print_list(head2)

# Merge the two sorted linked lists
merged_head = mergeSort(head1, head2)

print("Merged sorted linked list:")
print_list(merged_head)
