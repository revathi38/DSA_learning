class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtFront(self, data):  # O(1)
        newNode = Node(data)
        temp = self.head
        newNode.next = temp
        self.head = newNode
        return self.head

    def insertAtEnd(self, data):  # O(N)
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return self.head

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = newNode
        return self.head

    def getLength(self):  # O(N)
        temp = self.head
        count = 0

        while temp:
            count += 1
            temp = temp.next

        print(count)
        return count

    def inerstAtK(self, data, position):  # O(N)
        newNode = Node(data)

        if position < 0 and position > self.getLength():
            return self.head

        if position == 0:
            newNode.next = self.head
            self.head = newNode
            return self.head

        temp = self.head

        for i in range(position-1):
            temp = temp.next

        newNode.next = temp.next
        temp.next = newNode
        return self.head

    def removeAtK(self, position):  # O(N)
        if position < 0 or position > self.getLength():
            return self.head

        if position == 0:
            self.head = self.head.next
            return self.head

        temp = self.head

        for i in range(position-1):
            temp = temp.next

        temp.next = temp.next.next
        return self.head

    def search(self, data):
        temp = self.head

        while temp:
            if temp.val == data:
                return True
            temp = temp.next
        return False

    # print list

    def printList(self):  # O(N)
        temp = self.head
        res = ""

        while temp:
            if temp.next:
                res += str(temp.val) + " --> "
            else:
                res += str(temp.val)
            temp = temp.next
        print(res)


LL = LinkedList()
LL.insertAtFront(3)
LL.insertAtFront(4)
LL.insertAtFront(8)
LL.insertAtEnd(10)
LL.inerstAtK(12, 2)
LL.removeAtK(1)
LL.printList()
LL.getLength()
print(LL.search(12))
