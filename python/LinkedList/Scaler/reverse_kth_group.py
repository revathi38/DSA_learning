class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def reverse_kth_group(head, k):
    if not head or not head.next:
        return head

    curr = head
    prev = None
    count = k

    while curr and count > 0:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
        count -= 1

    if curr:
        head.next = reverse_kth_group(curr, k)

    return prev

# Function to print the linked list


def print_list(head):
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()


# Example usage
# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> None
root = Node(1)
root.next = Node(2)
root.next.next = Node(3)
root.next.next.next = Node(4)
root.next.next.next.next = Node(5)
root.next.next.next.next.next = Node(6)
root.next.next.next.next.next.next = Node(7)
root.next.next.next.next.next.next.next = Node(8)

print("Original linked list:")
print_list(root)

# Reverse the k group nodes
k = 3
root = reverse_kth_group(root, k)

print("After reversing the first", k, "nodes:")
print_list(root)
