"""
Problem Description
Given a linked list where every node represents a linked list and contains two pointers of its type:

Pointer to next node in the main list (right pointer)
Pointer to a linked list where this node is head (down pointer). All linked lists are sorted.
You are asked to flatten the linked list into a single list. Use down pointer to link nodes of the flattened list. The flattened linked list should also be sorted.



Problem Constraints
1 <= Total nodes in the list <= 100000

1 <= Value of node <= 109



Input Format
The only argument given is head pointer of the doubly linked list.



Output Format
Return the head pointer of the Flattened list.



Example Input
Input 1:

   3 -> 4 -> 20 -> 20 ->30
   |    |    |     |    |
   7    11   22    20   31
   |               |    |
   7               28   39
   |               |
   8               39
Input 2:

   2 -> 4 
   |    |       
   7    11    
   |            
   7


Example Output
Output 1:

 3 -> 4 -> 7 -> 7 -> 8 -> 11 -> 20 -> 20 -> 20 -> 22 -> 28 -> 30 -> 31 -> 39 -> 39 
Output 2:

 2 -> 4 -> 7 -> 7 -> 11
"""


class Node:
    def __init__(self, value):
        self.val = value
        self.right = None  # Pointer to the next node in the main list
        self.down = None   # Pointer to the linked list where this node is the head


def flattenLinkedList(head):
    if not head or not head.right:
        return head

    curr = head

    return merge(curr, flattenLinkedList(curr.right))


def merge(x, y):
    if x is None:
        return y
    if y is None:
        return x
    if x.val < y.val:
        ans = x
        x_down = merge(x.down, y)
        ans.down = x_down
    else:
        ans = y
        y_down = merge(y.down, x)
        ans.down = y_down

    return ans


def print_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.down
    print()


# Create nodes for the first example input
node1 = Node(3)
node1.down = Node(7)
node1.down.down = Node(8)
node1.right = Node(4)
node1.right.down = Node(11)
node1.right.down.down = Node(39)
node1.right.right = Node(20)
node1.right.right.down = Node(22)
node1.right.right.down.down = Node(28)
node1.right.right.right = Node(20)
node1.right.right.right.down = Node(20)
node1.right.right.right.down.down = Node(39)
node1.right.right.right.right = Node(30)
node1.right.right.right.right.down = Node(31)


root1 = flattenLinkedList(node1)
print_list(root1)

# Create nodes for the second example input
node2 = Node(2)
node2.down = Node(7)
node2.down.down = Node(7)
node2.right = Node(4)
node2.right.down = Node(11)


root2 = flattenLinkedList(node2)
print_list(root2)


# TC: O(N)
# SC: O(1)
