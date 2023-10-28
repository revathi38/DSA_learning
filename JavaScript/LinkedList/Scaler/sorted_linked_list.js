class Node {
  constructor(val, next = null) {
    this.val = val;
    this.next = next;
  }
}

function splitLL(head) {
  if (!head || !head.next) {
    return head;
  }

  let mid = middleElement(head);
  let nextPart = mid.next;

  mid.next = null;

  let left = splitLL(head);
  let right = splitLL(nextPart);

  const sortedList = merge(left, right);
  return sortedList;
}

function middleElement(head) {
  let slow = head;
  let fast = head;

  while (fast && fast.next && fast.next.next) {
    slow = slow.next;
    fast = fast.next.next;
  }

  return slow;
}

function merge(h1, h2) {
  if (!h1 && !h2) {
    return null;
  }

  const dummyNode = new Node(0);
  let curr = dummyNode;

  while (h1 && h2) {
    if (h1.val <= h2.val) {
      curr.next = h1;
      h1 = h1.next;
    } else {
      curr.next = h2;
      h2 = h2.next;
    }
    curr = curr.next;
  }

  if (h1) {
    curr.next = h1;
  }

  if (h2) {
    curr.next = h2;
  }

  return dummyNode.next;
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

// # Example usage
// # Create the first sorted linked list: 1 -> 3 -> 5 -> 7 -> None
let head = new Node(4);
head.next = new Node(2);
head.next.next = new Node(1);
head.next.next.next = new Node(3);
head.next.next.next.next = new Node(5);

console.log("Original linked list:");
printList(head);

// # Sort the linked list
const sorted_head = splitLL(head);

console.log("Sorted linked list:");
printList(sorted_head);
