class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def reverse_kth_group(head, k):
    count = 0
    temp = head

    while temp and count < k:
        temp = temp.next
        count += 1

    if count < k:
        return head

    prev = None
    current = head

    for _ in range(k):
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    # Recursively reverse the next group
    head.next = reverse_kth_group(current, k)
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
