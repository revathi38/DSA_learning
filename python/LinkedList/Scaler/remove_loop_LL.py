"""
Problem Description
You are given a linked list that contains a loop.
You need to find the node, which creates a loop and break it by making the node point to NULL.



Problem Constraints
1 <= number of nodes <= 1000



Input Format
The first of the input contains a LinkedList, where the first number is the number of nodes N, and the next N nodes are the node value of the linked list.
The second line of the input contains an integer which denotes the position of node where cycle starts.



Output Format
return the head of the updated linked list.



Example Input
Input 1:

 
1 -> 2
^    |
| - - 
Input 2:

3 -> 2 -> 4 -> 5 -> 6
          ^         |
          |         |    
          - - - - - -


Example Output
Output 1:

 1 -> 2 -> NULL
Output 2:

 3 -> 2 -> 4 -> 5 -> 6 -> NULL
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def removeLoop(head):

    if not head or not head.next:
        return head
    
    slow = head
    fast = head
    hasCycle = False
    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            hasCycle = True
            break 

    if not hasCycle:
        return head
    
    if head == fast:
        while head != fast.next:
            fast = fast.next
        fast.next = None

        return head
        

    prev = None
    slow = head

    while slow != fast:
        slow = slow.next
        prev = fast
        fast = fast.next

    if prev:
        prev.next = None

    return head
        


# Function to print the linked list
def print_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print()


headNode = Node(1)
headNode.next = Node(2)
headNode.next.next = Node(3)
headNode.next.next.next = Node(4)
headNode.next.next.next.next = Node(5)
headNode.next.next.next.next.next = Node(6)
headNode.next.next.next.next.next.next = Node(7)
headNode.next.next.next.next.next.next.next = Node(8)
headNode.next.next.next.next.next.next.next.next = Node(9)
headNode.next.next.next.next.next.next.next.next.next = headNode.next.next.next
root = removeLoop(headNode)
print_list(root)


