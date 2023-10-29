class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

function isPalindrome(head) {
  // Find the middle element using the slow and fast pointers
  let slow = head;
  let fast = head;

  while (fast && fast.next && fast.next.next) {
    slow = slow.next;
    fast = fast.next.next;
  }

  // Reverse the linked list from the middle element
  let prev = null;
  let curr = slow;

  while (curr) {
    let nextNode = curr.next;
    curr.next = prev;
    prev = curr;
    curr = nextNode;
  }

  // Check head node and prev node values
  while (head) {
    if (head.val !== prev.val) {
      return false;
    }
    head = head.next;
    prev = prev.next;
  }

  return true;
}

// Create nodes for the linked list
let headNode = new Node("M");
headNode.next = new Node("M");
headNode.next.next = new Node("A");
headNode.next.next.next = new Node("D");
headNode.next.next.next.next = new Node("A");
headNode.next.next.next.next.next = new Node("M");
headNode.next.next.next.next.next.next = new Node("M");

console.log(isPalindrome(headNode));

// TC: O(N)
// SC: O(1)
