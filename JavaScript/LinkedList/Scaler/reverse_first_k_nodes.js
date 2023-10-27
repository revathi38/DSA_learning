class Node {
  constructor(val, next = null) {
    this.val = val;
    this.next = next;
  }
}

function reverse_first_k_nodes(head, k) {
  let curr = head;
  let prev = null;

  while (curr && k > 0) {
    let nextNode = curr.next;
    curr.next = prev;
    prev = curr;
    curr = nextNode;
    k -= 1;
  }

  head.next = curr;
  return prev;
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

//  Example usage
//   Create a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> None
let root = new Node(1);
root.next = new Node(2);
root.next.next = new Node(3);
root.next.next.next = new Node(4);
root.next.next.next.next = new Node(5);
root.next.next.next.next.next = new Node(6);
root.next.next.next.next.next.next = new Node(7);
root.next.next.next.next.next.next.next = new Node(8);

console.log("Original linked list:");
printList(root);

const k = 3;
// # Reverse Linked List
const rootNode = reverse_first_k_nodes(root, k);

console.log("After reversing the first " + k + " nodes:");
printList(rootNode);
