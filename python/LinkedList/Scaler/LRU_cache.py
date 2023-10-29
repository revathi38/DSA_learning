class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def set(self, key, value):
        newNode = Node(key, value)
        self.cache[key] = newNode
        self.insert(newNode)

        if len(self.cache) > self.capacity:
            node = self.head.next
            self.remove(node)
            del self.cache[node.key]

    def get(self, key):
        if key in self.cache:
            selected_node = self.cache[key]
            self.remove(selected_node)
            self.insert(selected_node)
            return selected_node.value
        return -1

    def insert(self, node):
        prevNode = self.tail.prev

        prevNode.next = node
        self.tail.prev = node

        node.prev = prevNode
        node.next = self.tail

    def remove(self, node):
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode

    def print_list(self):
        current = self.head.next
        while current:
            print(current.key, " ", current.value, end=" ")
            current = current.next
        print()

    def cacheData(self):
        for k, v in self.cache.items():
            print(k, "", v.key, v.value, end=" ")
        print()


lru = LRUCache(2)
lru.set(1, 10)
lru.set(2, 20)
print(lru.get(1))  # 10
print(lru.get(2))  # 20
print(lru.get(5))  # -1
lru.set(4, 70)
print(lru.get(4))  # 70
print(lru.get(1))  # -1
lru.set(1, 15)
print(lru.get(1))
(lru.print_list())
lru.cacheData()
