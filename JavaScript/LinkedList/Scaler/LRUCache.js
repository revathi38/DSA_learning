class Node {
  constructor(key, value) {
    this.key = key;
    this.value = value;
    this.next = null;
    this.prev = null;
  }
}

class LRUCache {
  constructor(capacity) {
    this.head = new Node(-1, -1);
    this.tail = new Node(-1, -1);

    this.capacity = capacity;
    this.cache = {};

    this.head.next = this.tail;
    this.tail.prev = this.head;
  }

  get(key) {
    if (key in this.cache) {
      let selectedNode = this.cache[key];

      this.remove(selectedNode);
      this.insert(selectedNode);

      return selectedNode.value;
    }
    return -1;
  }

  set(key, value) {
    let newNode = new Node(key, value);
    this.cache[key] = newNode;
    this.insert(newNode);

    if (Object.keys(this.cache).length > this.capacity) {
      let node = this.head.next;
      this.remove(node);

      delete this.cache[node.key];
    }
  }

  insert(node) {
    let previousNode = this.tail.prev;
    previousNode.next = node;
    node.next = this.tail;

    this.tail.prev = node;
    node.prev = this.head;
  }

  remove(node) {
    let previousNode = node.prev;
    let nextNode = node.next;

    previousNode.next = nextNode;
    nextNode.prev = previousNode;
  }
}

let lru = new LRUCache(2);
lru.set(1, 10);
lru.set(2, 40);
console.log(lru.get(1)); // 10
console.log(lru.get(2)); // 40
console.log(lru.get(19)); //-1
lru.set(5, 90);
console.log(lru.get(5)); // 90
console.log(lru.get(1)); // -1
console.log(lru.get(2)); // 40
lru.set(1, 17);
console.log(lru.get(1)); //17
