class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

function removeLoop(head) {
  if (!head || !head.next) {
    return head;
  }

  let slow = head;
  let fast = head;
  let hasCycle = false;

  while (fast && fast.next && fast.next.next) {
    slow = slow.next;
    fast = fast.next.next;
    if (slow == fast) {
      hasCycle = true;
      break;
    }
  }

  if (!hasCycle) {
    return head;
  }

  if (head == fast) {
    while (fast.next != head) {
      fast = fast.next;
    }
    fast.next = null;
    return head;
  }

  let prev = null;
  slow = head;

  while (slow.val != fast.val) {
    prev = fast;
    slow = slow.next;
    fast = fast.next;
  }

  if (prev) {
    prev.next = null;
  }
  return head;
}

// # Function to print the linked list
function printList(head) {
  let current = head;
  while (current) {
    process.stdout.write(current.val + " -> "); // Equivalent to Python's end=" "
    current = current.next;
  }
  console.log(); // Print a newline character to move to the next line
}

// Create a linked list with a cycle: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 1 (connecting back to node 3)
const headNode = new Node(1);
headNode.next = new Node(2);
headNode.next.next = new Node(3);
headNode.next.next.next = new Node(4);
headNode.next.next.next.next = new Node(5);
headNode.next.next.next.next.next = new Node(6);
headNode.next.next.next.next.next.next = new Node(7);
headNode.next.next.next.next.next.next.next = new Node(8);
headNode.next.next.next.next.next.next.next.next = new Node(9);
headNode.next.next.next.next.next.next.next.next.next = headNode; // Creating a cycle

// Detect cycle in the linked list
const root = removeLoop(headNode);
printList(root);
