class Node {
  constructor(value) {
    this.val = value;
    this.right = null; // Pointer to the next node in the main list
    this.down = null; // Pointer to the linked list where this node is the head
  }
}

function flattenLinkedList(head) {
  if (!head || !head.right) {
    return head;
  }

  let curr = head;

  return merge(curr, flattenLinkedList(curr.right));
}

function merge(x, y) {
  if (!x) {
    return y;
  }
  if (!y) {
    return x;
  }
  let ans;
  if (x.val < y.val) {
    ans = x;
    let x_down = merge(x.down, y);
    ans.down = x_down;
  } else {
    ans = y;
    let y_down = merge(y.down, x);
    ans.down = y_down;
  }

  return ans;
}

function printList(head) {
  let current = head;
  while (current) {
    process.stdout.write(current.val + " -> ");
    current = current.down;
  }
  console.log();
}

// Create nodes for the first example input
let node1 = new Node(3);
node1.down = new Node(7);
node1.down.down = new Node(8);
node1.right = new Node(4);
node1.right.down = new Node(11);
node1.right.down.down = new Node(39);
node1.right.right = new Node(20);
node1.right.right.down = new Node(22);
node1.right.right.down.down = new Node(28);
node1.right.right.right = new Node(20);
node1.right.right.right.down = new Node(20);
node1.right.right.right.down.down = new Node(39);
node1.right.right.right.right = new Node(30);
node1.right.right.right.right.down = new Node(31);

let root1 = flattenLinkedList(node1);
printList(root1);

// Create nodes for the second example input
let node2 = new Node(2);
node2.down = new Node(7);
node2.down.down = new Node(7);
node2.right = new Node(4);
node2.right.down = new Node(11);

let root2 = flattenLinkedList(node2);
printList(root2);

// TC: O(N)
// SC: O(1)
