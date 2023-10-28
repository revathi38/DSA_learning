class Node {
  constructor(val, next = null) {
    this.val = val;
    this.next = next;
  }
}

function mergeSort(h1, h2) {
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
let head1 = new Node(1);
head1.next = new Node(3);
head1.next.next = new Node(5);
head1.next.next.next = new Node(7);

// # Create the second sorted linked list: 2 -> 4 -> 6 -> None
let head2 = new Node(2);
head2.next = new Node(4);
head2.next.next = new Node(6);

console.log("First sorted linked list:");
printList(head1);

console.log("Second sorted linked list:");
printList(head2);

// # Merge the two sorted linked lists
const merged_head = mergeSort(head1, head2);

console.log("Merged sorted linked list:");
printList(merged_head);
