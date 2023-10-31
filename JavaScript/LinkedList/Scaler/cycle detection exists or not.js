class Node {
  constructor(data, next = null) {
    this.val = data;
    this.next = next;
  }
}

function detectCycle(head) {
  if (!head) {
    return false;
  }

  let slowPointer = head;
  let fastPointer = head;

  while (fastPointer && fastPointer.next && fastPointer.next.next) {
    slowPointer = slowPointer.next;
    fastPointer = fastPointer.next.next;

    if (slowPointer === fastPointer) {
      return true;
    }
  }

  return false;
}

// Example usage
// Create a linked list with a cycle: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 3 (connecting back to node 3)
const head = new Node(1);
head.next = new Node(2);
head.next.next = new Node(3);
head.next.next.next = new Node(4);
head.next.next.next.next = new Node(5);
head.next.next.next.next.next = new Node(6);
head.next.next.next.next.next.next = head.next.next; // Creating a cycle

// Detect cycle in the linked list
const hasCycle = detectCycle(head);

if (hasCycle) {
  console.log("Cycle detected in the linked list.");
} else {
  console.log("No cycle detected in the linked list.");
}

// TC: O(N)
// SC: O(1)
